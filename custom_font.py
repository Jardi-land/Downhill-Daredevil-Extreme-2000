# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame

import alias as al
from spritesheet import SpriteSheet


class Font:
    """Une classe représentant une police de caractères.

    Parameters:
    -----------
    ss : SpriteSheet
        L'objet SpriteSheet contenant les images des caractères de la police.
    scale : int, optional
        L'échelle à appliquer à la police de caractères.

    Attributes:
    -----------
    spritesheet : SpriteSheet
        L'objet SpriteSheet contenant les images des caractères de la police.
    scale : int
        L'échelle à appliquer à la police de caractères.
    space : int
        L'espace entre chaque caractère.
    surface_dict : dict
        Un dictionnaire contenant les surfaces Pygame de chaque caractère.
    possible_letters : list
        Une liste de tous les caractères possibles dans la police de caractères.

    Methods:
    --------
    render(string: str = "", catch: str = "") -> pygame.Surface:
        Rend la chaîne de caractères donnée sous forme de surface Pygame.
    """

    def __init__(self,
                 ss: SpriteSheet,
                 scale: int = 1) -> None:

        self.spritesheet = ss

        self.scale = scale

        self.space = 0 * self.scale

        self.surface_dict = {}

        self.possible_letters = []

        for letter in self.spritesheet.data:
            self.surface_dict[letter] = self.spritesheet.parse_sprite(
                info=letter)
            self.possible_letters.append(letter)

        self.__resize()

    def __resize(self):
        for surface in self.surface_dict:
            _ = (self.surface_dict[surface].get_width(
            ) * self.scale, self.surface_dict[surface].get_height() * self.scale)
            self.surface_dict[surface] = al.im_scale(
                self.surface_dict[surface], _)
            del _

    def render(self, string: str = "", catch: str = ""):
        surface_size = pygame.math.Vector2(0, 14*self.scale)
        for letter in string:
            if letter in self.possible_letters:
                surface_size.x += self.surface_dict[letter].get_width() + \
                    self.space
            else:
                surface_size.x += self.surface_dict[catch].get_width() + \
                    self.space

        surface = pygame.Surface(surface_size).convert_alpha()
        surface.fill((0, 0, 0, 0))

        self.letter_x = 0
        for letter in string:

            if letter in self.possible_letters:
                surface.blit(self.surface_dict[letter], (self.letter_x, 0))
                self.letter_x += self.surface_dict[letter].get_width() + \
                    self.space
            else:
                surface.blit(self.surface_dict[catch], (self.letter_x, 0))
                self.letter_x += self.surface_dict[catch].get_width() + \
                    self.space

        return surface
