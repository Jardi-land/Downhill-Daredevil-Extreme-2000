# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame  # Import de la libraire pygame
import json  # Import de la libraire json

import alias as al


class SpriteSheet:
    """
    Classe représentant une feuille de sprites.

    Attributes:
    -----------
    filename : str
        Le chemin d'accès du fichier de la feuille de sprites.
    sprite_sheet : pygame.Surface
        L'image de la feuille de sprites chargée et convertie en mode alpha.
    meta_data : str
        Le chemin d'accès du fichier JSON contenant les informations sur la feuille de sprites.
    data : dict
        Un dictionnaire contenant les informations sur la feuille de sprites extraites du fichier JSON.

    Methods:
    --------
    get_sprite(x, y, w, h)
        Renvoie une surface Pygame contenant le sprite de la feuille de sprites aux coordonnées (x, y) avec une largeur w et une hauteur h.

    parse_sprite(animation_name="", frame="", animation=False, info=[])
        Analyse les données de la feuille de sprites et renvoie le sprite correspondant en tant qu'image.

        Parameters:
        -----------
        animation_name : str, optional
            Le nom de l'animation à laquelle appartient le sprite.
        frame : str, optional
            Le nom du cadre de l'animation correspondant au sprite.
        animation : bool, optional
            Un indicateur indiquant si le sprite est destiné à être utilisé dans une animation.
        info : list, optional
            Une liste contenant les clés du dictionnaire de données correspondant à l'emplacement du sprite.

        Returns:
        --------
        image : pygame.Surface
            Une surface Pygame contenant le sprite de la feuille de sprites correspondant aux paramètres donnés.
    """

    def __init__(self, filepath, jsonfile):
        """
        Initialise une instance de la classe spritesheet.

        Parameters:
        -----------
        filepath : str
            Le chemin d'accès du fichier de la feuille de sprites.
        jsonfile : str
            Le chemin d'accès du fichier JSON contenant les informations sur la feuille de sprites.
        """
        self.filename = filepath
        self.sprite_sheet = al.im_load(filepath).convert_alpha()
        self.meta_data = jsonfile
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()

    def get_sprite(self, x: int, y: int, w: int, h: int):
        """
        Renvoie une surface Pygame contenant le sprite de la feuille de sprites aux coordonnées (x, y) avec une largeur w et une hauteur h.

        Parameters:
        -----------
        x : int
            La position horizontale du sprite sur la feuille de sprites.
        y : int
            La position verticale du sprite sur la feuille de sprites.
        w : int
            La largeur du sprite.
        h : int
            La hauteur du sprite.

        Returns:
        --------
        sprite : pygame.Surface
            Une surface Pygame contenant le sprite de la feuille de sprites aux coordonnées (x, y) avec une largeur w et une hauteur h.
        """
        sprite = pygame.Surface((w, h)).convert_alpha()
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        return sprite

    def parse_sprite(self, animation_name="", frame="", animation=False, info=[]):
        """Analyse les données de la feuille de sprites et renvoie le sprite correspondant en tant qu'image.

        Parameters:
        -----------
        animation_name : str, optional
            Le nom de l'animation à laquelle appartient le sprite.
        frame : str, optional
            Le nom du cadre de l'animation correspondant au sprite.
        animation : bool, optional
            Un indicateur indiquant si le sprite est destiné à être utilisé dans une animation.
        info : list, optional
            Une liste contenant les clés du dictionnaire de données correspondant à l'emplacement du sprite.

        Returns:
        --------
        image : pygame.Surface
            Une surface Pygame contenant le sprite de la feuille de sprites correspondant aux paramètres donnés.
        """
        if animation:
            sprite = self.data[animation_name][frame]["frame"]
        else:
            _ = self.data
            for key in info:
                _ = _[key]
            sprite = _
            del _
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h)
        return image
