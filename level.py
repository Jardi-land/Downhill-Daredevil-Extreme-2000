# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame  # Import de la librairie pygame
import json  # Import de la librairie json
import random # Import de la librairie random

import alias as al
from player import Player
from map import Map
from camera import Camera
from score import Score


class Level:
    def __init__(self) -> None:
        
        from input import Input_global
        self.input_global = Input_global
        
        self.player = Player()
        self.camera = Camera(self.player.image, self.player.pos, self.player.rect, self.player.track)
        self.score = Score()

        self.__load_maps()
        self.__load_spawn()
        self.__init_chuck()
        
        self.__camera_init()
        

    def __load_maps(self):
        with open(al.path("files/maps/data.json"), "r") as f:
            self.maps_data = json.load(f)

        self.maps = {}

        for map in self.maps_data:
            self.maps[map] = {"map": Map(
                al.path(f"files/maps/tmx/{map}.tmx")), "weight": self.maps_data[map]["weight"]}
            
    def __load_spawn(self):
        self.spawn_map = Map(al.path("files/maps/tmx/spawn.tmx"))
        
    def __init_chuck(self):
        self.chunk_turn = "a"
        self.chunk_list = [self.spawn_map]
        
        self.possible_chunk = []
        
        for map in self.maps:
            for i in range(self.maps[map]["weight"]*3):
                self.possible_chunk.append(map)
                random.shuffle(self.possible_chunk)
                    
        for i in range(len(self.possible_chunk)):
            self.chunk_list.append(Map(al.path(f"files/maps/tmx/{self.possible_chunk[0]}.tmx")))
            self.possible_chunk.pop(0)
            
    def __camera_init(self):
        self.camera.spawn_map = self.spawn_map
        self.camera.calc_vector_offset()
        
    def forward(self):
        self.camera.vector_offset.y -= self.player.current_speed
        self.score.score += self.player.current_speed/10
        print(f"Vitesse : {round(self.player.current_speed, 2)}m/s")
        self.score.score_interne += self.player.current_speed/10
        if self.score.score_interne > self.player.current_speed*15:
            self.score.score_interne = 0
            self.player.current_speed += 1
            print(self.player.current_speed)
        self.camera.score = self.score.update()

    
    def check_player_status(self):
        if self.camera.player_status == "dead":
            self.player.status = "dead"
            
    def check_player_bonus(self):
        if self.camera.bonus_hit:
            print(int(self.player.current_speed/5))
            self.player.current_speed -= int(self.player.current_speed/5)
            self.camera.bonus_hit = False
            self.player.bonus_toggle()
    
    def update(self):
        self.check_player_bonus()
        self.check_player_status()
        self.player.update()
        self.camera.player_image = self.player.image
        self.camera.player_pos = self.player.pos
        self.forward()
        self.camera.player_speed = self.player.current_speed
        return self.camera.draw(self.chunk_list)
