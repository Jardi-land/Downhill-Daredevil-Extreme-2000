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

    window = pygame.display.set_mode((300, 150))

    pygame.display.set_caption("Crash Report - Lz_framework")

    clock = pygame.time.Clock()

    pygame.mouse.set_visible(True)

    window_icon = al.im_scale(al.im_load(
        f"file/icon/{'icon_win' if platform.system() == 'Windows' else 'icon_li'}.png"), (512, 512))

    pygame.display.set_icon(window_icon)

    surface = pygame.Surface(
        (window.get_width()/2, window.get_height()/2)).convert_alpha()

    font = pygame.font.Font("file/font/KenneyMini.ttf",
                            8, bold=False, italic=False)

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

    webbrowser.open(f"mailto:{crash_report_mail}?Subject={crash_report_subject}&body={crash_report_body.format(win_name=window_name, crash_rep=crash_report, plat_sys=platform.system(), dt_now=dt.now(), plat_ver=platform.version(), plat_arch=platform.architecture(), plat_proc=platform.processor(), plat_pyth_ver=platform.python_version())}")

    while True:

        # Get every pygame event
        for event in pygame.event.get():

            # Catch the quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        window.blit(al.im_scale(surface, (300, 150)), (0, 0))

        pygame.display.flip()

        clock.tick(60)
