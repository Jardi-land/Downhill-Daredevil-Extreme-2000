# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame  # Import de la libraire pygame
import os
import sys


def im_load(path: str = "") -> pygame.Surface:
    """
    Charge une image à partir du chemin spécifié et renvoie une surface Pygame avec une transparence.

    Args:
        path (str, optionnel): Le chemin vers le fichier image. Par défaut, "".

    Returns:
        pygame.Surface: Un objet surface Pygame avec de la transparence.
    """
    return pygame.image.load(path).convert_alpha()


def im_scale(image: pygame.Surface, size: tuple = (0, 0)) -> pygame.Surface:
    """
    Redimensionne une surface Pygame à la taille spécifiée.

    Args:
        image (pygame.Surface): La surface Pygame à redimensionner.
        size (tuple, optionnel): La taille de la surface redimensionnée. Par défaut, (0, 0).

    Returns:
        pygame.Surface: La surface Pygame redimensionnée.
    """
    return pygame.transform.scale(image, size)

def abso_path(path: str) -> str:
    """
    Transforme un chemin d'accés relatif en chemin d'accés absolut

    Args:
        path (str): Le chemin d'accés à modifier

    Returns:
        str: Le chemin d'accés absolut
    """
    return os.path.join(os.path.dirname(sys.argv[0]), path)
