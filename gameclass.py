# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame  # Import de la libraire pygame

import alias as al
from menu import Menu
from level import Level


class GameClass:
    """
    Classe représentant un jeu.

    Attributes:
        surface (pygame.Surface): La surface du jeu.
        surface_scale (pygame.Surface): La surface redimensionnée du jeu.
        screen_size (tuple): La taille de la surface du jeu (largeur, hauteur).

    Methods:
        draw(surface: pygame.Surface) -> None:
            Dessine le jeu sur la surface spécifiée.
    """
    def __init__(self) -> None:
        """
        Initialise une instance de la classe GameClass.
        """
        self.surface = pygame.Surface((1920, 1080))
        self.surface.fill((0, 0, 0, 0))
        self.surface_scale = self.surface.copy()

        self.screen_size = (1920, 1080)
        
        self.menu = Menu()
        self.level = Level()
        
        self.in_game = False
        self.clicked = False
        self.button_disappear = 10

    def __draw_on_surface(self) -> None:
        """
        Dessine le jeu sur la surface du jeu.

        Returns:
            None
        """
        # Draw the Game on self.surface

        self.surface.blit(self.level.update(), (0, 0))
        if not self.in_game:
            self.surface.blit(self.menu.draw(), (0, 0))

    def __resize(self) -> None:
        """
        Redimensionne la surface du jeu.

        Returns:
            None
        """
        if self.screen_size != self.surface.get_size():
            self.surface_scale = al.im_scale(self.surface, self.screen_size)
        else:
            self.surface_scale = self.surface.copy()
            
    def update(self):
        if not self.in_game:
            if self.clicked:
                self.button_disappear -= 1
            if self.menu.update() is not None:
                self.clicked = True
                
            if self.button_disappear == 0:
                self.in_game = True
                self.level.player.current_speed = self.level.player.initial_speed
    

    def draw(self, surface: pygame.Surface) -> None:
        """
        Dessine le jeu sur la surface spécifiée.

        Args:
            surface (pygame.Surface): La surface sur laquelle le jeu doit être dessiné.

        Returns:
            None
        """
        self.__draw_on_surface()
        self.__resize()
        self.update()
        surface.blit(self.surface_scale, (0, 0))
