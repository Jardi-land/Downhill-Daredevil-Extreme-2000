# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame  # Import de la libraire pygame

from spritesheet import SpriteSheet
import alias as al
from custom_font import Font



class Score:
    def __init__(self) -> None:
        self.font_spritesheet = SpriteSheet(al.path("files/font/custom/tilesheet.png"), al.path("files/font/custom/data.json"))
        
        self.font = Font(self.font_spritesheet, 6)
        
        self.surface = pygame.Surface((1920, 1200)).convert_alpha()
        self.surface.fill((0, 0, 0, 0))
        
        self.score = 0
        
        self.score_surface = self.font.render(str(self.score))
        
        self.surface.blit(self.score_surface, (self.surface.get_width() - self.score_surface.get_width(), 0))
        
    def render_text(self):
        self.score_surface = self.font.render(str(int(self.score)))
        self.surface = pygame.Surface((1920, 1200)).convert_alpha()
        self.surface.fill((0, 0, 0, 0))
        self.surface.blit(self.score_surface, (self.surface.get_width() - self.score_surface.get_width(), 0))
        
    def update(self, surface):
        self.render_text()
        surface.blit(self.surface, (0, 0))
        return surface
