# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame  # Import de la libraire pygame
import platform  # Import de la librairie platform
import webbrowser  # Import de la librairie webbrowserß
from datetime import datetime as dt  # Import de la librairie datetime

import alias as al
# from settings import * (future module)


def main(crash_report: str) -> None:
    """
    Affiche une fenêtre d'erreur en cas de crash du programme. Ouvre automatiquement l'application de messagerie avec un nouveau message contenant un rapport d'erreur.

    Args:
        crash_report (str): Le message d'erreur à inclure dans le rapport envoyé par email.

    Returns:
        None.
    """
    # Définition des variables
    window = pygame.display.set_mode((300, 150))

    # Définition du nom de la fenêtre
    pygame.display.set_caption("Crash Report")

    # Définition de la vitesse de rafraîchissement de la fenêtre
    clock = pygame.time.Clock()

    # Définition de l'affichage du curseur de la souris
    pygame.mouse.set_visible(True)

    # Création de la surface de la fenêtre
    surface = pygame.Surface(
        (window.get_width()/2, window.get_height()/2)).convert_alpha()

    # Définition de la police d'écriture
    font = pygame.font.Font("file/font/KenneyMini.ttf",
                            8, bold=False, italic=False)

    # Render du texte
    font_render = font.render(
        f"{window_name} a rencontré une", True, pygame.Color(255, 255, 255))
    font_render_2 = font.render(
        f"erreur durant son", True, pygame.Color(255, 255, 255))
    font_render_2_2 = font.render(
        f"exécution.", True, pygame.Color(255, 255, 255))

    font_render_3 = font.render(
        f"Merci d'envoyer le", True, pygame.Color(255, 255, 255))
    font_render_4 = font.render(
        f"mail ouvert ", True, pygame.Color(255, 255, 255))
    font_render_5 = font.render(
        f"automatiquement.", True, pygame.Color(255, 255, 255))

    # Affichage du texte
    surface.blit(font_render, (surface.get_width() /
                 2 - font_render.get_width()/2, 5))
    surface.blit(font_render_2, (surface.get_width() /
                 2 - font_render_2.get_width()/2, 15))
    surface.blit(font_render_2_2, (surface.get_width() /
                 2 - font_render_2_2.get_width()/2, 25))
    surface.blit(font_render_3, (surface.get_width() /
                 2 - font_render_3.get_width()/2, 35))
    surface.blit(font_render_4, (surface.get_width() /
                 2 - font_render_4.get_width()/2, 45))
    surface.blit(font_render_5, (surface.get_width() /
                 2 - font_render_5.get_width()/2, 55))

    # Ouvre l'application de messagerie avec un nouveau message contenant un rapport d'erreur
    webbrowser.open(f"mailto:{crash_report_mail}?Subject={crash_report_subject}&body={crash_report_body.format(win_name=window_name, crash_rep=crash_report, plat_sys=platform.system(), dt_now=dt.now(), plat_ver=platform.version(), plat_arch=platform.architecture(), plat_proc=platform.processor(), plat_pyth_ver=platform.python_version())}")

    # Boucle principale
    while True:

        # Gestion des évènements
        for event in pygame.event.get():

            # Gestion de la fermeture de la fenêtre
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Affichage du texte
        window.blit(al.im_scale(surface, (300, 150)), (0, 0))

        # Rafraichissement de la fenêtre
        pygame.display.flip()

        # Définition de la vitesse de rafraîchissement de la fenêtre sur 60 FPS
        clock.tick(60)
