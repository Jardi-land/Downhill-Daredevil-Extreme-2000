# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------


import pygame  # Import pygame library
from pygame import mixer  # Import mixer from pygame library


import alias as al  # Import alias.py
# Import SpriteSheet class from spritesheet.py
from spritesheet import SpriteSheet


def palette_swap(surf, old_color, new_color):
    """Effectue un échange de palette sur une surface donnée.

    Args:
        surf (pygame.Surface): La surface sur laquelle effectuer l'échange de palette.
        old_color (Tuple[int, int, int]): La couleur existante à remplacer, spécifiée en tant que tuple (R, G, B).
        new_color (Tuple[int, int, int]): La nouvelle couleur à utiliser, spécifiée en tant que tuple (R, G, B).

    Returns:
        pygame.Surface: Une copie de la surface modifiée avec les couleurs remplacées.

    Raises:
        None

    Exemple:
        surface = pygame.image.load('image.png')
        ancienne_couleur = (255, 0, 0)  # Rouge
        nouvelle_couleur = (0, 255, 0)  # Vert
        nouvelle_surface = palette_swap(surface, ancienne_couleur, nouvelle_couleur)
    """
    img_copy = pygame.Surface(surf.get_size())
    img_copy.fill(new_color)
    surf.set_colorkey(old_color)
    img_copy.blit(surf, (0, 0))
    return img_copy


class Button:
    """Représente un bouton interactif avec du texte sur une surface.

    Attributes:
        text (pygame.Surface): La surface contenant le texte à afficher sur le bouton.
        pos (tuple): La position du bouton, spécifiée en tant que tuple (x, y).
        ui_spritesheet (SpriteSheet): La feuille de sprites utilisée pour les éléments graphiques du bouton.
        action (str): L'action associée au bouton lorsque celui-ci est cliqué.
        lock (bool): Indique si le bouton est verrouillé ou non.

    Methods:
        check_mouse(): Vérifie si la souris est positionnée sur le bouton.
        click_action(): Vérifie si le bouton est cliqué.
        update(): Met à jour l'apparence du bouton en fonction de son état.
        get_action(): Renvoie l'action associée au bouton si celui-ci est cliqué.
        draw(): Dessine le bouton et renvoie sa surface actuelle.

    Example:
        button = Button(text=my_text_surface, pos=(100, 200), ui_spritesheet=my_spritesheet, action="start_game")
        button.draw()
    """

    def __init__(self,
                 text: pygame.Surface = None,
                 pos: tuple = (0, 0),
                 ui_spritesheet: SpriteSheet = None,
                 action: str = None,
                 lock=False):

        from input import Input_global
        self.input_global = Input_global

        self.text = text

        self.lock = lock

        self.pos = pos

        self.scale = (480, 270)

        self.action = action

        self.mouse_pos = None

        self.size = (self.text.get_width(), self.text.get_height())

        mixer.init()
        self.select_sound = mixer.Sound(al.path("files/sound/select.mp3"))
        self.sound_played = False

        self.button_surface_dict = {"corner_top_left": ui_spritesheet.parse_sprite(info=["corner_top_left"]),
                                    "corner_top_right": ui_spritesheet.parse_sprite(info=["corner_top_right"]),
                                    "top": ui_spritesheet.parse_sprite(info=["top"]),
                                    "left": ui_spritesheet.parse_sprite(info=["left"]),
                                    "right": ui_spritesheet.parse_sprite(info=["right"]),
                                    "center": ui_spritesheet.parse_sprite(info=["center"]),
                                    "corner_bottom_left": ui_spritesheet.parse_sprite(info=["corner_bottom_left"]),
                                    "corner_bottom_right": ui_spritesheet.parse_sprite(info=["corner_bottom_right"]),
                                    "bottom": ui_spritesheet.parse_sprite(info=["bottom"]),
                                    "corner_bottom_left_click": ui_spritesheet.parse_sprite(info=["corner_bottom_left_click"]),
                                    "corner_bottom_right_click": ui_spritesheet.parse_sprite(info=["corner_bottom_right_click"]),
                                    "bottom_click": ui_spritesheet.parse_sprite(info=["bottom_click"])}

        self.surface = pygame.Surface(
            (self.size[0] + 8, self.size[1] + 8)).convert_alpha()
        self.surface.fill((0, 0, 0, 0))

        self.surface.blit(self.button_surface_dict["corner_top_left"], (0, 0))
        self.surface.blit(self.button_surface_dict["corner_top_right"], (self.surface.get_width(
        ) - self.button_surface_dict["corner_top_right"].get_width(), 0))
        for i in range(self.surface.get_width() - 6):
            self.surface.blit(self.button_surface_dict["top"], (i + 3, 0))
            self.surface.blit(self.button_surface_dict["bottom"], (
                i + 3, self.surface.get_height() - self.button_surface_dict["bottom"].get_height()))
        for i in range(self.surface.get_height() - 8):
            self.surface.blit(self.button_surface_dict["left"], (0, i + 3))
            self.surface.blit(self.button_surface_dict["right"], (self.surface.get_width(
            ) - self.button_surface_dict["right"].get_width(), i + 3))
        self.surface.blit(self.button_surface_dict["corner_bottom_left"], (0, self.surface.get_height(
        ) - self.button_surface_dict["corner_bottom_left"].get_height()))
        self.surface.blit(self.button_surface_dict["corner_bottom_right"], (self.surface.get_width(
        ) - self.button_surface_dict["corner_bottom_right"].get_width(), self.surface.get_height() - self.button_surface_dict["corner_bottom_right"].get_height()))
        self.surface.blit(al.im_scale(
            self.button_surface_dict["center"], (self.size[0] + 2, self.size[1] + 2)), (3, 2))

        self.mask = pygame.mask.from_surface(self.surface)
        self.mask_outline = self.mask.outline()
        self.mask_surf = self.mask.to_surface().convert_alpha()
        self.mask_surf.fill((0, 0, 0, 0))
        for pixel in self.mask_outline:
            self.mask_surf.set_at(pixel, (255, 255, 255))

        self.surface_with_mask = self.surface.copy()
        self.surface_with_mask.blit(self.mask_surf, (0, 0))

        self.surface_click = self.surface_with_mask.copy()

        self.surface_click.blit(self.button_surface_dict["corner_bottom_left_click"], (0, self.surface_click.get_height(
        ) - self.button_surface_dict["corner_bottom_left_click"].get_height()))
        self.surface_click.blit(self.button_surface_dict["corner_bottom_right_click"], (self.surface_click.get_width(
        ) - self.button_surface_dict["corner_bottom_right_click"].get_width(), self.surface_click.get_height() - self.button_surface_dict["corner_bottom_right_click"].get_height()))
        for i in range(self.surface.get_width() - 6):
            self.surface_click.blit(self.button_surface_dict["bottom_click"], (
                i + 3, self.surface.get_height() - self.button_surface_dict["bottom_click"].get_height()))

        self.surface_click.blit(self.mask_surf, (0, 0))

        if not self.lock:
            self.surface.blit(self.text, (4.5, 3))
        self.surface_with_mask.blit(self.text, (4.5, 3))
        self.surface_click.blit(self.text, (4.5, 4))

        self.grey = self.surface.copy()
        self.grey_mask = pygame.mask.from_surface(self.grey)
        self.grey_mask_surface = self.grey_mask.to_surface(
            setcolor=(34, 34, 34, 140)).convert_alpha()
        palette_swap(self.grey_mask_surface, (0, 0, 0), (0, 0, 0, 0))

        self.blit_mask = False

        self.current_surface = self.surface

    def check_mouse(self):
        self.mouse_pos = self.input_global.get_mouse_pos()

        if self.mouse_pos[0] >= self.input_global.scale_converter(self.scale, self.pos)[0] and self.mouse_pos[0] <= self.input_global.scale_converter(self.scale, self.pos)[0] + self.input_global.scale_converter(self.scale, (self.size[0] + 8, self.size[1] + 8))[0] and self.mouse_pos[1] >= self.input_global.scale_converter(self.scale, self.pos)[1] and self.mouse_pos[1] <= self.input_global.scale_converter(self.scale, self.pos)[1] + self.input_global.scale_converter(self.scale, (self.size[0] + 8, self.size[1] + 8))[1]:
            self.blit_mask = True
            return True
        else:
            self.blit_mask = False
            return False

    def click_action(self):
        self.mouse = self.input_global.get_mouse_button_pressed(0)

        if self.mouse:
            return True
        else:
            return False

    def update(self):
        if self.lock:
            return self.surface
        if True:
            if self.check_mouse():
                if self.click_action():
                    if self.sound_played == False:
                        self.sound_played = True
                        mixer.Sound.play(self.select_sound)
                    self.current_surface = self.surface_click
                else:
                    self.current_surface = self.surface_with_mask
            else:
                self.current_surface = self.surface

            return self.current_surface

    def get_action(self):
        if self.current_surface == self.surface_click:
            return self.action
        else:
            return None

    def draw(self):

        return self.update()
