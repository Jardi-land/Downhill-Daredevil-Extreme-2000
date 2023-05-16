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
        
        self.score = 0
        self.score_interne = 0
        
        self.score_surface = self.font.render(str(self.score))
        
    def render_text(self):
        self.score_surface = self.font.render(str(int(self.score)))
        
    def update(self):
        self.render_text()
        return self.score_surface