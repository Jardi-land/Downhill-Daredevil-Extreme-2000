# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame  # Import de la libraire pygame

from custom_font import Font
from spritesheet import SpriteSheet
import alias as al
from button import Button


class Menu:
    def __init__(self) -> None:
        self.surface = pygame.Surface((480, 270)).convert_alpha()
        self.surface.fill((0, 0, 0, 0))

        self.font_spritesheet = SpriteSheet(al.path(
            "files/font/custom/tilesheet.png"), al.path("files/font/custom/data.json"))

        self.font = Font(self.font_spritesheet, 1.5)

        self.ui_spritesheet = SpriteSheet(
            al.path("files/maps/texture/tilemap.png"), al.path("files/ui/data.json"))

        self.play_text = self.font.render("PLAY", "#")

        self.play_button = Button(
            self.play_text, (480/2, 355/2), self.ui_spritesheet, "play")

        self.play_button = Button(self.play_text, (480/2 - self.play_button.draw().get_width(
        )/2, 355/2 - self.play_button.draw().get_height()/2), self.ui_spritesheet, "play")

    def update(self):
        if self.play_button.get_action() is not None:
            return self.play_button.get_action()

    def draw(self):
        self.surface.blit(self.play_button.draw(),
                          (self.play_button.pos[0], self.play_button.pos[1]))
        return al.im_scale(self.surface, (1920, 1080))


class DeathScreen:
    def __init__(self, score, best) -> None:
        self.surface = pygame.Surface((480, 270)).convert_alpha()
        self.surface.fill((0, 0, 0, 0))

        self.font_spritesheet = SpriteSheet(al.path(
            "files/font/custom/tilesheet.png"), al.path("files/font/custom/data.json"))

        self.font_1 = Font(self.font_spritesheet, 5)
        self.font = Font(self.font_spritesheet, 2)
        self.font_2 = Font(self.font_spritesheet, 1)

        self.ui_spritesheet = SpriteSheet(
            al.path("files/maps/texture/tilemap.png"), al.path("files/ui/data.json"))

        self.background_text = self.font_1.render("DIED", "#")

        self.background_button = Button(
            self.background_text, (480/2, 270/2), self.ui_spritesheet, "Null")

        self.background_button = Button(self.background_text, (480/2 - self.background_button.draw().get_width(
        )/2, 270/2 - self.background_button.draw().get_height()/2), self.ui_spritesheet, "Null", True)

        self.game_over_text = self.font.render("GAME OVER", "#")

        self.score_text = self.font_2.render(f"SCORE: {score}", "#")

        self.best_text = self.font_2.render(f"BEST: {best}", "#")

        self.replay_text = self.font_2.render("REPLAY", "#")

        self.replay_button = Button(
            self.replay_text, (480/2, 200), self.ui_spritesheet, "play")

        self.replay_button = Button(self.replay_text, (480/2 - self.replay_button.draw().get_width(
        )/2, 200 - self.replay_button.draw().get_height()/2), self.ui_spritesheet, "play")

        self.slash = al.im_turn(al.im_load(al.path("files/ui/slash.png")), -90)

        self.slash_x = 481

        self.slash_surface = al.im_load(al.path("files/ui/slash_surface.png"))

        self.fade_in = False
        self.new_game = False

    def update(self):
        if self.replay_button.get_action() is not None:
            return self.replay_button.get_action()

    def draw(self):
        self.surface.blit(self.background_button.update(
        ), (self.background_button.pos[0], self.background_button.pos[1]))
        self.surface.blit(self.game_over_text, (480/2 - self.game_over_text.get_width() /
                          2, 135/2 - self.game_over_text.get_height()/2))
        self.surface.blit(
            self.score_text, (480/2 - self.score_text.get_width()/2, self.background_button.pos[1] + 10))
        self.surface.blit(self.best_text, (480/2 - self.score_text.get_width()/2,
                          self.background_button.pos[1] + self.background_button.size[1] - 20))
        self.surface.blit(self.replay_button.update(
        ), (self.replay_button.pos[0], self.replay_button.pos[1]))

        if self.fade_in:
            if not self.slash_x < -self.slash.get_width():
                self.slash_x -= 59
            else:
                self.new_game = True

        return al.im_scale(self.surface, (1920, 1080))
