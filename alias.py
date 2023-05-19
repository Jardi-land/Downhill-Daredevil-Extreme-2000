# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame  # Import de la libraire pygame
import os  # Import de la librairie os
import sys  # Import de la librairie sys


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


def im_turn(image: pygame.Surface, angle: int = 0) -> pygame.Surface:
    """
    Tourne une surface Pygame à l'angle spécifié.

    Args:
        image (pygame.Surface): La surface Pygame à tourner.
        angle (int, optionnel): L'angle de rotation de la surface. Par défaut, 0.

    Returns:
        pygame.Surface: La surface Pygame tournée.
    """
    return pygame.transform.rotate(image, angle)


def path(path: str) -> str:
    """
    Connecte le chemin d'accés

    Args:
        path (str): Le chemin d'accés à modifier

    Returns:
        str: Le chemin d'accés connecté
    """
    return os.path.join(os.path.dirname(sys.argv[0]), path)

def filecheck(path: str) -> bool:
    """
    Vérifie si le fichier existe
    
    Args:
        path (str): Le chemin d'accés à vérifier
        
    Returns:
        bool: True si le fichier existe, False sinon
    """
    return os.path.isfile(path)
