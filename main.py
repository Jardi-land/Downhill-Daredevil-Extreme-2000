# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame  # Import de la libraire pygame
from pygame.locals import *  # Import des constantes de pygame
import os  # Import de la librairie os
import platform  # Import de la librairie platform
import traceback  # Import de la librairie traceback

from gameclass import GameClass
import crash_catch
import alias as al
from settings import *


def game_loop(fullscreen: bool = False,
              name: str = os.path.dirname(__file__),
              mouse_visible: bool = True,
              icon_type: int = 0,
              icon_path: dict = {}) -> None:
    """
    Boucle principale d'un jeu en Pygame.

    Args:
        fullscreen (bool): Indique si le jeu doit être en plein écran ou non. False par défaut.
        name (str): Le nom de la fenêtre du jeu. Par défaut, le nom est le nom du répertoire qui contient le fichier.
        mouse_visible (bool): Indique si le curseur de la souris est visible ou non. True par défaut.
        icon_type (int): Le type d'icône à utiliser pour la fenêtre. 0 pour aucune icône, 1 pour une icône pour toutes les plateformes, 2 pour des icônes différentes pour des plateformes différentes. 0 par défaut.
        icon_path (dict): Un dictionnaire contenant les chemins d'accès aux icônes pour les différentes plateformes. Le dictionnaire doit contenir une clé "Windows" et une clé "other". {} par défaut.

    Returns:
        None

    Raises:
        ValueError: Si icon_type est différent de 0, 1 ou 2, ou si icon_path n'est pas un dictionnaire.

    """

    # Initialisation de pygame
    pygame.init()

    # Création de la fenêtre du jeu
    window = pygame.display.set_mode((0, 0),
                                     (HWSURFACE | DOUBLEBUF) | FULLSCREEN if fullscreen else RESIZABLE)

    from input import Input_global
    from debug import Debug_overlay

    # Définition du nom de la fenêtre
    pygame.display.set_caption(name)

    # Définition de la vitesse de rafraîchissement de la fenêtre
    clock = pygame.time.Clock()

    # Définition de l'affichage du curseur de la souris
    pygame.mouse.set_visible(mouse_visible)

    # Définition de l'icône de la fenêtre en fonction de icon_type
    match icon_type:
        # Dans le cas icon_type = 0, aucune icône n'est chargée
        case 0:
            pass

        # Dans le cas icon_type = 1, une icône est chargée pour toutes les plateformes
        case 1:
            icon_path = icon_path.values()[0]

            icon = al.im_load(icon_path)

            # Définition de l'icône de la fenêtre
            pygame.display.set_icon(icon)

        # Dans le cas icon_type = 2, une icône est chargée pour Windows et une autre pour les autres plateformes
        case 2:
            if icon_path == {} or icon_path is None:
                raise ValueError("icon_path must be a dictionary")
            icon_path = icon_path["Windows" if platform.system() == "Windows"
                                  else "other"]

            icon = al.im_load(icon_path)

            # Définition de l'icône de la fenêtre
            pygame.display.set_icon(icon)

        # Dans le cas icon_type est différent de 0, 1 ou 2, une erreur est levée
        case other:
            raise ValueError(f"icon_type must be 0, 1 or 2 not {other}")

    # Object Game class ici
    # ----------------------
    Game = GameClass()
    # ----------------------

    # Une fois que le jeu est prêt, on lance la boucle principale
    while True:
        # Récupération des événements pygame
        for event in pygame.event.get():
            # Si l'événement est VIDEORESIZE, on affiche les nouvelles dimensions de la fenêtre
            if event.type == VIDEORESIZE:
                Game.screen_size = (event.w, event.h)
            # Si l'événement est QUIT, on quitte le jeu et python
            if event.type == QUIT:
                pygame.quit()
                exit()

        # Update de l'input
        # -----------------
        Input_global.frame_begin(window.get_size())
        # -----------------

        # Game class object update here
        # -----------------------------
        Game.draw(window)
        Debug_overlay.update(f"FPS: {clock.get_fps():.2f}")
        pygame.display.set_caption(f"FPS: {clock.get_fps():.2f}")
        # -----------------------------

        # Update de l'input
        # -----------------
        Input_global.frame_end()
        # -----------------

        # Debug overlay ici (si besoin)
        # -----------------------
        #Debug_overlay.draw(window)
        # -----------------------

        # Update de la fenêtre
        pygame.display.flip()
        # On limite le nombre de rafraîchissement de la fenêtre à 60 fps
        clock.tick(60)


# Si le fichier est exécuté, on lance la boucle principale
if __name__ == "__main__":
    try:
        game_loop(fullscreen=False,
                  name=f"{window_name}",
                  mouse_visible=True,
                  icon_type=2,
                  icon_path={"Windows": al.path("files/icon/png/icon_win.png"), "other": al.path("files/icon/png/icon_osx.png")})
    # Si une erreur est levée, on la capture et on la transmet à crash_catch
    except Exception as e:
        print(traceback.format_exc())
        crash_catch.main(crash_report=traceback.format_exc())
