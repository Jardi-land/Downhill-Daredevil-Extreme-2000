# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame  # Import de la libraire pygame


def im_load(path: str = "") -> pygame.Surface:
    """
    Charge une image depuis un chemin de fichier donné et retourne un objet Surface de Pygame.\n
    ! Pas besoin de convert_alpha() car la fonction le fait déjà. !

    Args:
        path (str): Le chemin d'accès du fichier image à charger. Par défaut, c'est une chaîne de caractères vide.

    Returns:
        pygame.Surface: Un objet Surface de Pygame représentant l'image chargée.

    Raises:
        Toutes les exceptions levées par la méthode pygame.image.load().
    """
    return pygame.image.load(path).convert_alpha()


def im_scale(image: pygame.Surface, size: tuple = (0, 0)) -> pygame.Surface:
    """
    Redimensionne une image donnée à la taille spécifiée et retourne un objet Surface de Pygame représentant l'image redimensionnée.

    Args:
        image (pygame.Surface): L'objet Surface de Pygame représentant l'image à redimensionner.
        size (tuple): Le tuple spécifiant la taille de l'image redimensionnée. Par défaut, c'est (0, 0).

    Returns:
        pygame.Surface: Un objet Surface de Pygame représentant l'image redimensionnée.

    Raises:
        Toutes les exceptions levées par la méthode pygame.transform.scale().
    """
    return pygame.transform.scale(image, size)
