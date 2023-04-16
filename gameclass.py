# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame  # Import de la libraire pygame

import alias as al


class GameClass:
    def __init__(self) -> None:
        self.surface = pygame.Surface((1920, 1080))
        self.surface.fill((0, 0, 0, 0))
        self.surface_scale = self.surface.copy()

        self.screen_size = (1920, 1080)

    def __draw_on_surface(self) -> None:

        # Draw the Game on self.surface

        pass

    def __resize(self) -> None:
        if self.screen_size != self.surface.get_size():
            self.surface_scale = al.im_scale(self.surface, self.screen_size)
        else:
            self.surface_scale = self.surface.copy()

    def draw(self, surface: pygame.Surface) -> None:
        self.__draw_on_surface()
        self.__resize()
        surface.blit(self.surface, (0, 0))
