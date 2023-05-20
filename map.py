# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame  # Import de la librairie pygame
from pytmx.util_pygame import load_pygame  # Import de la librairie pytmx

import alias as al


class Map:
    def __init__(self, tmx_path: str) -> None:

        self.map_data = load_pygame(tmx_path)

        self.scale = 6.75

        self.surfaces = {"down": pygame.Surface((self.map_data.width * self.map_data.tilewidth * self.scale, self.map_data.height * self.map_data.tileheight * self.scale)).convert_alpha(),
                         "up": pygame.Surface((self.map_data.width * self.map_data.tilewidth * self.scale, self.map_data.height * self.map_data.tileheight * self.scale)).convert_alpha()}
        
        self.surfaces["down"].fill((0, 0, 0, 0))
        self.surfaces["up"].fill((0, 0, 0, 0))

        self.layers = {"background": self.map_data.get_layer_by_name("background"),
                       "obstacle": self.map_data.get_layer_by_name("obstacle")}
        
        self.layers_array = {
            "background": "down",
            "obstacle": "up",
            "deco": "down",
        }
        
        self.bonus = False
        
        self.__check_layer("deco")
        self.__check_layer("bonus")

        self.__draw()
        
        self.colliders_list = []
        
        self.__set_colliders()

    def __check_layer(self, layer_name: str):
        for layer in self.map_data.visible_layers:
            if layer.name == layer_name:
                self.layers[layer_name] = layer


    def __draw(self):
        for layer in self.layers:
            match layer:
                case "bonus":
                    self.speed_minus_rect = pygame.rect.Rect(self.map_data.get_object_by_name("speed_minus").x*self.scale, self.map_data.get_object_by_name("speed_minus").y*self.scale, self.map_data.get_object_by_name("speed_minus").width*self.scale, self.map_data.get_object_by_name("speed_minus").height*self.scale)
                    self.speed_minus_pos = (self.map_data.get_object_by_name("speed_minus").x*self.scale, self.map_data.get_object_by_name("speed_minus").y*self.scale)
                    self.bonus = True
                case other:
                    for x, y, surf in self.layers[layer].tiles():
                        self.surfaces[self.layers_array[other]].blit(al.im_scale(surf, (surf.get_width()*self.scale, surf.get_height(
                        )*self.scale)), (x * self.map_data.tilewidth * self.scale, y * self.map_data.tileheight * self.scale))
                        
    def __set_colliders(self):
        for gid, tile_obj_g in self.map_data.get_tile_colliders():
            for collider in tile_obj_g:
                for x,y,layer_index in self.map_data.get_tile_locations_by_gid(gid):
                    print(collider.x, collider.y)
                    self.colliders_list.append({"pos": (x*16*self.scale + collider.x*self.scale, y*16*self.scale + collider.y*self.scale), "rect":pygame.Rect(collider.x*self.scale, collider.y*self.scale, collider.width*self.scale, collider.height*self.scale)})
