# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------


import pygame  # Import de la librairie pygame

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
                "idle_mask": {
                    "1": al.im_scale(self.spritesheet.parse_sprite(info=["green", "idle_mask", "1"]), (16*6.75, 16*6.75)),
                    "2": al.im_scale(self.spritesheet.parse_sprite(info=["green", "idle_mask", "2"]), (16*6.75, 16*6.75)),
                    "3": al.im_scale(self.spritesheet.parse_sprite(info=["green", "idle_mask", "3"]), (16*6.75, 16*6.75)),
                    "4": al.im_scale(self.spritesheet.parse_sprite(info=["green", "idle_mask", "4"]), (16*6.75, 16*6.75)),
                    "5": al.im_scale(self.spritesheet.parse_sprite(info=["green", "idle_mask", "5"]), (16*6.75, 16*6.75)),
                },
                "push": al.im_scale(self.spritesheet.parse_sprite(info=["green", "push"]), (16*6.75, 16*6.75))
            },
            "purple": {
                "idle": al.im_scale(self.spritesheet.parse_sprite(info=["purple", "idle"]), (16*6.75, 16*6.75)),
                "push": al.im_scale(self.spritesheet.parse_sprite(info=["purple", "push"]), (16*6.75, 16*6.75))
            }
        }

        self.player_type = "green"
        self.player_state = "idle"
        self.player_mask_total = 5
        self.player_mask_index = 1
        self.player_mask_speed = 0.25

        self.image = self.images[self.player_type][self.player_state]

        self.initial_speed = 10
        self.current_speed = 0

        self.rect = pygame.rect.Rect(
            0, 0, self.image.get_width() - 30, self.image.get_height()/2)

        self.spawn_pos = pygame.math.Vector2(1920/2, 700/2)
        self.pos = self.spawn_pos

        self.left_rect = None
        self.right_rect = None

        self.status = "alive"

        self.dead_index = 10

        self.track = al.im_scale(self.spritesheet.parse_sprite(
            info=["track"]), (16*6.75, 16*6.75))

        self.bonus_anim = False

    def movement(self):
        if not self.pos.x < 50:
            if self.input_global.get_pressed("a"):
                self.pos.x = self.pos.x-self.current_speed
            else:
                if self.left_rect is not None:
                    self.left_rect = None

        if not self.pos.x > 1870:
            if self.input_global.get_pressed("d"):
                self.pos.x = self.pos.x+self.current_speed
            else:
                if self.right_rect is not None:
                    self.right_rect = None

    def dead_animation(self):
        if self.dead_index == 0:
            if self.image.get_alpha() == 0:
                self.image.set_alpha(255)
            else:
                self.image.set_alpha(0)
            self.dead_index = 10

        self.dead_index -= 1

    def bonus_toggle(self):
        self.bonus_anim = True

    def bonus_animation(self):
        self.image = self.images[self.player_type]["idle_mask"][str(
            int(self.player_mask_index))]
        self.player_mask_index += self.player_mask_speed
        if int(self.player_mask_index) == self.player_mask_total + 1:
            self.player_mask_index = 1
            self.bonus_anim = False
            self.image = self.images[self.player_type]["idle"]

    def update(self):
        if self.bonus_anim:
            self.bonus_animation()
        if self.status == "alive":
            self.movement()
            self.rect.centerx = self.pos.x
            self.rect.centery = self.pos.y-self.image.get_height()/4
        else:
            self.current_speed = 0
            self.dead_animation()
