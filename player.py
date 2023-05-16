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
        
        from input import Input_global
        self.input_global = Input_global
        
        self.spritesheet = SpriteSheet(al.path(
            "files/players/texture/players.png"), al.path("files/players/data.json"))
        
        self.images = {
            "green": {
                "idle": al.im_scale(self.spritesheet.parse_sprite(info=["green", "idle"]), (16*6.75, 16*6.75)),
                "push": al.im_scale(self.spritesheet.parse_sprite(info=["green", "push"]), (16*6.75, 16*6.75))
            },
            "purple": {
                "idle": al.im_scale(self.spritesheet.parse_sprite(info=["purple", "idle"]), (16*6.75, 16*6.75)),
                "push": al.im_scale(self.spritesheet.parse_sprite(info=["purple", "push"]), (16*6.75, 16*6.75))
            }
        }
        
        self.player_type = "green"
        self.player_state = "idle"

        self.image = self.images[self.player_type][self.player_state]
        
        self.initial_speed = 10
        self.current_speed = self.initial_speed
        
        self.rect = pygame.rect.Rect(0, 0, self.image.get_width(), self.image.get_height()/2)
        
        self.spawn_pos = pygame.math.Vector2(1920/2, 1200/2)
        self.pos = self.spawn_pos
        
        self.left_rect = None
        self.right_rect = None
        
        self.status = "alive"
        
        self.dead_index = 10
        
    def movement(self):
        if not self.pos.x < 50:
            if self.input_global.get_pressed("a"):
                self.pos.x = self.pos.x-self.current_speed
                self.left_rect = pygame.rect.Rect(self.rect.left-self.current_speed, self.rect.top, self.current_speed, self.image.get_height()/2+self.current_speed)
            else:
                if self.left_rect is not None:
                    self.left_rect = None
        
        if not self.pos.x > 1870:
            if self.input_global.get_pressed("d"):
                self.pos.x = self.pos.x+self.current_speed
                self.right_rect = pygame.rect.Rect(self.rect.right, self.rect.top, self.current_speed, self.image.get_height()/2+self.current_speed)
            else:
                if self.right_rect is not None:
                    self.right_rect = None
                
        self.down_rect = pygame.rect.Rect(self.rect.left, self.rect.bottom, self.image.get_width(), self.current_speed)
            
    def dead_animation(self):
        if self.dead_index == 0:
            if self.image.get_alpha() == 0:
                self.image.set_alpha(255)
            else:
                self.image.set_alpha(0)
            self.dead_index = 10
            
        self.dead_index -= 1
        
         
    def update(self):
        if self.status == "alive":
            self.movement()
            self.rect.centerx = self.pos.x
            self.rect.centery = self.pos.y-self.image.get_height()/4
        else:
            self.current_speed = 0
            self.dead_animation()
