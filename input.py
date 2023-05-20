# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame  # Import de la librairie pygame


class Keyboard:
    """
    Classe qui représente le clavier de l'utilisateur.

    Elle contient un dictionnaire qui associe chaque touche du clavier à son code.

    Attributes:
        key_code (dict): Un dictionnaire qui associe chaque touche du clavier à son code.

    Methods:
        __init__(): Initialise l'objet keyboard et remplit le dictionnaire key_code avec les codes de chaque touche du clavier.
    """

    def __init__(self) -> None:

        self.key_code = {}

        for i in range(len(pygame.key.get_pressed())):
            self.key_code[pygame.key.name(i)] = i


class Input:
    """
    Classe qui gère l'entrée utilisateur en jeu.

    Attributs :
        list_begin (dict) : dictionnaire contenant les états des périphériques en début de frame.
        list_end (dict) : dictionnaire contenant les états des périphériques en fin de frame.
        keyboard (Keyboard) : instance de la classe Keyboard qui gère l'état des touches du clavier.

    Méthodes :
        __init__() : initialise les attributs list_begin, list_end et keyboard.
        frame_begin() : met à jour les états des périphériques en début de frame.
        frame_end() : met à jour les états des périphériques en fin de frame.
        test_key(key:str) -> bool : vérifie si la touche 'key' existe et renvoie True si c'est le cas.
        get_pressed(key:str) -> bool : renvoie True si la touche 'key' est enfoncée en début de frame.
        get_released(key:str) -> bool : renvoie True si la touche 'key' a été relâchée entre le début et la fin de frame.
        get_mouse_pos() -> Vector2 : renvoie la position de la souris en début de frame.
        get_mouse_button_pressed(index:int) -> bool : renvoie True si le bouton 'index' de la souris est enfoncé en début de frame.
        get_mouse_button_released(index:int) -> bool : renvoie True si le bouton 'index' de la souris a été relâché entre le début et la fin de frame.

    """

    def __init__(self) -> None:
        # Création des dictionnaires qui contiendront les états des périphériques en début de frame
        self.list_begin = {"joystick": {}, "keyboard": {},
                           "mouse": {"pos": (0, 0), "buttons": (0, 0, 0)}}

        # Création du dictionnaire qui contiendra les états des périphériques en fin de frame
        self.list_end = {"joystick": {}, "keyboard": {},
                         "mouse": {"pos": (0, 0), "buttons": (0, 0, 0)}}

        # Création de l'objet Keyboard
        self.keyboard = Keyboard()

        # Initialisation des dictionnaires
        self.list_begin["keyboard"] = pygame.key.get_pressed()
        self.list_begin["mouse"]["pos"] = pygame.mouse.get_pos()
        self.list_begin["mouse"]["buttons"] = pygame.mouse.get_pressed()

        # Initialisation des dictionnaires
        self.list_end["keyboard"] = pygame.key.get_pressed()
        self.list_end["mouse"]["buttons"] = pygame.mouse.get_pressed()

        self.window_size = pygame.math.Vector2(0, 0)

    def frame_begin(self, size) -> None:
        """
        Met à jour les états du clavier et de la souris et stocke les valeurs actuelles dans la liste de début.

        Args:
            Aucun argument n'est attendu.

        Returns:
            None.
        """
        self.list_begin["keyboard"] = pygame.key.get_pressed()
        self.list_begin["mouse"]["pos"] = pygame.mouse.get_pos()
        self.list_begin["mouse"]["buttons"] = pygame.mouse.get_pressed()
        self.window_size.x, self.window_size.y = size[0], size[1]

    def frame_end(self) -> None:
        """
        Met à jour les états du clavier et de la souris et stocke les valeurs actuelles dans la liste de début.

        Args:
            Aucun argument n'est attendu.

        Returns:
            None.
        """
        self.list_end["keyboard"] = pygame.key.get_pressed()
        self.list_end["mouse"]["buttons"] = pygame.mouse.get_pressed()

    def __test_key(self, key: str) -> bool:
        """
        Teste si une touche existe sur le clavier.

        Args:
            key (str): Le nom de la touche à tester.

        Returns:
            bool: True si la touche existe.

        Raises:
            ValueError: Si la touche n'est pas trouvée dans le dictionnaire des codes de touche.

        """
        _ = self.keyboard.key_code.get(key)
        if _ is None:
            del _
            raise ValueError(f"Input.py | Key '{key}' not found")
        else:
            del _
            return True

    def get_pressed(self, key: str) -> bool:
        """
        Retourne True si la touche spécifiée est enfoncée pendant cette image.

        Args:
            key (str): Le nom de la touche à vérifier.

        Returns:
            bool: True si la touche est enfoncée, False sinon.

        Raises:
            ValueError: Si le nom de la touche n'est pas reconnu.
        """
        if self.__test_key(key):
            return self.list_begin["keyboard"][self.keyboard.key_code.get(key)]

    def get_released(self, key: str) -> bool:
        """
        Vérifie si une touche a été relâchée depuis le dernier appel de frame_begin.

        Args:
            key (str): Nom de la touche.

        Returns:
            bool: True si la touche a été relâchée, False sinon.

        Raises:
            ValueError: Si la touche n'est pas trouvée dans la liste des touches du clavier.

        """
        if self.__test_key(key):
            if self.list_end["keyboard"][self.keyboard.key_code.get(key)] and not self.list_begin["keyboard"][self.keyboard.key_code.get(key)]:
                return True
            else:
                return False

    def get_mouse_pos(self) -> pygame.math.Vector2:
        """
        Renvoie la position actuelle de la souris.

        Returns:
            pygame.math.Vector2: un vecteur 2D contenant les coordonnées x et y de la souris.
        """
        return pygame.math.Vector2(self.list_begin["mouse"]["pos"])

    def get_mouse_button_pressed(self, index: int) -> bool:
        """
        Renvoie l'état du bouton de la souris spécifié par l'index.

        Args:
            index (int): Index du bouton de la souris à vérifier.
                0: clic gauche
                1: clic milieu
                2: clic droit

        Returns:
            bool: True si le bouton est enfoncé, False sinon.

        Raises:
            ValueError: si l'index n'est pas 0, 1 ou 2.

        """
        if index == 0 or index == 1 or index == 2:
            return self.list_begin["mouse"]["buttons"][index]
        else:
            raise ValueError(
                f"Input.py | Mouse button must be 0, 1 or 2 not {index}")

    def get_mouse_button_released(self, index: int) -> bool:
        """
        Renvoie un booléen indiquant si le bouton de la souris spécifié a été relâché entre les deux frames.

        Args:
            index (int): L'indice du bouton de la souris à vérifier.
                0: clic gauche
                1: clic milieu
                2: clic droit

        Returns:
            bool: True si le bouton de la souris spécifié a été relâché entre les deux frames, False sinon.

        Raises:
            ValueError: Si l'indice du bouton de la souris n'est pas 0, 1 ou 2.
        """
        if index == 0 or index == 1 or index == 2:
            if self.list_end["mouse"]["buttons"][index] and not self.list_begin["mouse"]["buttons"][index]:
                return True
            else:
                return False
        else:
            raise ValueError(
                f"Input.py | L'indice du bouton de la souris doit être 0, 1 ou 2 et non pas {index}.")

    def scale_converter(self, base_scale, pos):
        return (self.window_size.x*(pos[0] / base_scale[0]), self.window_size.y*(pos[1] / base_scale[1]))


# Création d'une instance de la classe Input
Input_global = Input()
