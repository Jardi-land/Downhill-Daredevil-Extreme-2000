# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------


import pygame  # Import de la librairie pygame
import json  # Import de la librairie json

from spritesheet import SpriteSheet
import alias as al


class Player:
    def __init__(self) -> None:
        self.spritesheet = SpriteSheet(al.path(
            "files/players/texture/players.png"), al.path("files/players/data.json"))
        
        self.images = {
            "green": {
                "idle": self.spritesheet.parse_sprite(info=["green", "idle"]),
                "push": self.spritesheet.parse_sprite(info=["green", "push"])
            },
            "purple": {
                "idle": self.spritesheet.parse_sprite(info=["purple", "idle"]),
                "push": self.spritesheet.parse_sprite(info=["purple", "push"])
            }
        }
        
        self.player_type = "green"
        self.player_state = "idle"

        self.image = self.images[self.player_type][self.player_state]
