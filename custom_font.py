# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame

import alias as al
from spritesheet import SpriteSheet


class Font:
    """
    Classe pour créer des surfaces de texte à partir d'un SpriteSheet.

    Attributes:
        spritesheet (SpriteSheet): Le SpriteSheet à utiliser pour le texte.
        scale (int): L'échelle à utiliser pour le texte. Par défaut, 1.
        space (int): L'espace à utiliser entre les lettres. Par défaut, 0.
        surface_dict (dict): Un dictionnaire contenant des surfaces de lettres.
        possible_letters (list): Une liste contenant toutes les lettres possibles.

    Methods:
        __init__(self, ss: SpriteSheet, scale: int = 1) -> None:
            Initialise la classe Font avec le SpriteSheet et l'échelle spécifiés.
        __resize(self) -> None:
            Redimensionne les surfaces de lettres dans le dictionnaire à l'échelle spécifiée.
        render(self, string: str = "", catch: str = "") -> pygame.Surface:
            Rend une surface de texte à partir d'une chaîne de caractères spécifiée.
    """

    def __init__(self,
                 ss: SpriteSheet,
                 scale: int = 1) -> None:
        """
        Initialise la classe Font avec le SpriteSheet et l'échelle spécifiés.

        Args:
            ss (SpriteSheet): Le SpriteSheet à utiliser pour le texte.
            scale (int, optionnel): L'échelle à utiliser pour le texte. Par défaut, 1.

        Returns:
            None
        """
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
        """
        Redimensionne les surfaces de lettres dans le dictionnaire à l'échelle spécifiée.

        Args:
            None

        Returns:
            None
        """
        for surface in self.surface_dict:
            _ = (self.surface_dict[surface].get_width(
            ) * self.scale, self.surface_dict[surface].get_height() * self.scale)
            self.surface_dict[surface] = al.im_scale(
                self.surface_dict[surface], _)
            del _

    def render(self, string: str = "", catch: str = ""):
        """
        Rend une surface de texte à partir d'une chaîne de caractères spécifiée.

        Args:
            string (str, optionnel): La chaîne de caractères à utiliser pour le texte. Par défaut, "".
            catch (str, optionnel): Le caractère à utiliser pour remplacer les lettres manquantes. Par défaut, "".

        Returns:
            pygame.Surface: Une surface de texte contenant la chaîne de caractères spécifiée.
        """
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
