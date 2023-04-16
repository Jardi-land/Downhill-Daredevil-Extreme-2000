# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame  # Import de la libraire pygame
import json  # Import de la libraire json

import alias as al


class SpriteSheet:
    """A class representing a sprite sheet image and its associated metadata.

    Attributes:
        filename (str): The filepath of the sprite sheet image.
        sprite_sheet (pygame.Surface): The loaded sprite sheet image.
        meta_data (str): The filepath of the associated JSON metadata file.
        data (dict): The parsed JSON metadata.

    Methods:
        get_sprite(x: int, y: int, w: int, h: int) -> pygame.Surface:
            Returns a surface containing a sprite at the specified position and dimensions.

        parse_sprite(animation_name: str="", frame: str="", animation: bool=False, info: List[str]=[]) -> pygame.Surface:
            Returns a surface containing the sprite associated with the specified metadata.

    Example:
        sprite_sheet = SpriteSheet("sprites.png", "sprites.json")
        idle_sprite = sprite_sheet.parse_sprite(animation_name="player", frame="idle")
        walking_sprite = sprite_sheet.parse_sprite(animation_name="player", frame="walking", animation=True)
    """

    def __init__(self, filepath, jsonfile):
        self.filename = filepath
        self.sprite_sheet = al.im_load(filepath).convert_alpha()
        self.meta_data = jsonfile
        with open(self.meta_data) as f:
            self.data = json.load(f)
        f.close()

    def get_sprite(self, x: int, y: int, w: int, h: int):
        sprite = pygame.Surface((w, h)).convert_alpha()
        sprite.blit(self.sprite_sheet, (0, 0), (x, y, w, h))
        return sprite

    def parse_sprite(self, animation_name="", frame="", animation=False, info=[]):
        if animation:
            sprite = self.data[animation_name][frame]["frame"]
        else:
            _ = self.data
            for key in info:
                _ = _[key]
            sprite = _
            del _
        x, y, w, h = sprite["x"], sprite["y"], sprite["w"], sprite["h"]
        image = self.get_sprite(x, y, w, h)
        return image
