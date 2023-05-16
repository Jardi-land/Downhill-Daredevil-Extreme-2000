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
        
        self.font_spritesheet = SpriteSheet(al.path("files/font/custom/tilesheet.png"), al.path("files/font/custom/data.json"))
        
        self.font = Font(self.font_spritesheet, 1)
        
        self.ui_spritesheet = SpriteSheet(al.path("files/maps/texture/tilemap.png"), al.path("files/ui/data.json"))
        
        self.play_text = self.font.render("PLAY", "#")
        
        self.play_button = Button(self.play_text, (480/2, 270/2), self.ui_spritesheet, "play")
        
        self.play_button = Button(self.play_text, (480/2 - self.play_button.draw().get_width()/2, 270/2 - self.play_button.draw().get_height()/2), self.ui_spritesheet, "play")
        
    def update(self):
        self.surface.blit(self.play_button.draw(), (self.play_button.pos[0], self.play_button.pos[1]))
        return al.im_scale(self.surface, (1920, 1080))

        
        
