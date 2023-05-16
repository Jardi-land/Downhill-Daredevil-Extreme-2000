# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame  # Import de la librairie pygame
import json  # Import de la librairie json
from pytmx.util_pygame import load_pygame  # Import de la librairie pytmx

import alias as al


class Map:
    def __init__(self, tmx_path: str) -> None:

        self.map_data = load_pygame(tmx_path)

        self.scale = 6.75

        self.surfaces = {"down": pygame.Surface((self.map_data.width * self.map_data.tilewidth * self.scale, self.map_data.height * self.map_data.tileheight * self.scale)).convert_alpha(),
                         "up": pygame.Surface((self.map_data.width * self.map_data.tilewidth * self.scale, self.map_data.height * self.map_data.tileheight * self.scale)).convert_alpha()}

        self.layers = {"background": self.map_data.get_layer_by_name("background"),
                       "obstacle": self.map_data.get_layer_by_name("obstacle")}
        self.__check_deco_layer()
        
        self.__draw()

    def __check_deco_layer(self):
        for layer in self.map_data.visible_layers:
            if layer.name == "deco":
                self.layers["deco"] = layer
                
    def __draw(self):
        for layer in self.layers:
            for x,y,surf in self.layers[layer].tiles():
                match layer:
                    case "background":
                        self.surfaces["down"].blit(al.im_scale(surf, (surf.get_width()*self.scale, surf.get_height()*self.scale)), (x * self.map_data.tilewidth * self.scale, y * self.map_data.tileheight * self.scale))
                    case "obstacle":
                        self.surfaces["up"].blit(al.im_scale(surf, (surf.get_width()*self.scale, surf.get_height()*self.scale)), (x * self.map_data.tilewidth * self.scale, y * self.map_data.tileheight * self.scale))
                    case "deco":
                        self.surfaces["down"].blit(al.im_scale(surf, (surf.get_width()*self.scale, surf.get_height()*self.scale)), (x * self.map_data.tilewidth * self.scale, y * self.map_data.tileheight * self.scale))
