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
        pass
