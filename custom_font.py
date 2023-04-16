# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame

import alias as al
from spritesheet import SpriteSheet


class Font:
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
