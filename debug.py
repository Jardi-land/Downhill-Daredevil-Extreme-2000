# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame  # Import de la libraire pygame


class Debug:
    """
    Classe Debug : permet d'afficher du texte à l'écran pour le débogage.

    Attributs :
        - surface : pygame.Surface, une surface pour afficher le texte
        - dict : dict, un dictionnaire stockant les textes à afficher
        - font : pygame.font.Font, la police utilisée pour afficher le texte

    Méthodes :
        - update(text: str) : Ajoute un texte à afficher dans le dictionnaire.
        - draw(surface: pygame.Surface) : Dessine les textes stockés sur la surface passée en paramètre et réinitialise le dictionnaire.
    """

    def __init__(self) -> None:
        # Création de la surface pour afficher le texte
        self.surface = pygame.Surface((1920, 1080)).convert_alpha()
        self.surface.fill((0, 0, 0, 0))

        # Création du dictionnaire qui contiendra les textes à afficher
        self.dict = {}

        # Création de la police pour afficher le texte
        self.font = pygame.font.Font("file/font/KenneyMini.ttf", 15)

    def update(self, text: str = ""):
        """
        Ajoute un texte dans le dictionnaire de messages de débogage.

        Args:
            text (str): Le texte à ajouter (par défaut: "").

        Returns:
            None
        """
        self.dict[len(self.dict.keys())] = str(text)

    def draw(self, surface: pygame.Surface):
        """
        Dessine le texte sur la surface spécifiée.

        Args:
            surface (pygame.Surface): La surface sur laquelle le texte doit être dessiné.

        Returns:
            None
        """
        # Réinitialisation de la surface
        self.surface.fill((0, 0, 0, 0))

        # Affichage des textes
        for k in self.dict.keys():
            self.surface.blit(self.font.render(
                self.dict[k], True, (0, 255, 0)), (10, k * 20))

        # Affichage de la surface sur la surface passée en paramètre
        surface.blit(self.surface, (0, 0))

        # Réinitialisation du dictionnaire
        self.dict = {}


# Création d'une instance de la classe Debug
debug_overlay = Debug()
