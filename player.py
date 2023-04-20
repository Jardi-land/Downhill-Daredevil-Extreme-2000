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
        with open(al.path("files/players/data.json"), "r") as file:
            self.spritesheet_data = json.load(file)
        file.close()
