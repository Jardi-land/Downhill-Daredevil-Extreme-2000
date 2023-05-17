# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame  # Import de la librairie pygame
from pygame import mixer

import alias as al


class Camera:
    def __init__(self, player_image, player_spawn_pos, player_rect) -> None:
        from debug import Debug_overlay
        self.debug = Debug_overlay
        self.surface = pygame.Surface((1920, 1080)).convert_alpha()
        self.player_image = player_image
        self.player_pos = pygame.math.Vector2(player_spawn_pos[0], player_spawn_pos[1])
        self.player_rect = player_rect
        self.player_status = "alive"
        
        mixer.init()
        
        self.hit_sound = mixer.Sound(al.path("files/sound/hit.mp3"))
        
        self.sound_played = False

    def calc_vector_offset(self):
        self.vector_offset = pygame.math.Vector2(0, 0)
        self.vector_offset.x = (self.surface.get_width(
        )/2) - (self.spawn_map.surfaces["down"].get_width()/2)
        self.vector_offset.y = (self.surface.get_height(
        )/2) - (self.spawn_map.surfaces["down"].get_height()/2)

    def draw(self, chunk_list):
        for value, chunk in enumerate(chunk_list):
            if self.vector_offset.y + (value*chunk.surfaces["down"].get_height()) > 2000 or self.vector_offset.y + (value*chunk.surfaces["down"].get_height()) < -2000:
                pass
            else:
                self.surface.blit(chunk.surfaces["down"], (self.vector_offset.x,
                                self.vector_offset.y + (value*chunk.surfaces["down"].get_height())))
        
        self.surface.blit(self.player_image, (self.player_pos.x - self.player_image.get_width()/2, self.player_pos.y - self.player_image.get_height()/2))
        
        for value, chunk in enumerate(chunk_list):
            if self.vector_offset.y + (value*chunk.surfaces["up"].get_height()) > 2000 or self.vector_offset.y + (value*chunk.surfaces["up"].get_height()) < -2000:
                pass
            else:
                self.surface.blit(chunk.surfaces["up"], (self.vector_offset.x,
                                self.vector_offset.y + (value*chunk.surfaces["up"].get_height())))
                for rect in chunk.colliders_list:
                    
                    rect["rect"].x = rect["pos"][0] + self.vector_offset.x
                    rect["rect"].y = rect["pos"][1] + (self.vector_offset.y + (value*chunk.surfaces["up"].get_height()))
                    if self.player_rect.colliderect(rect["rect"]):
                        self.player_status = "dead"
                        if self.sound_played == False:
                            self.sound_played = True
                            mixer.Sound.play(self.hit_sound)
                    if self.debug.debug_mode:
                        pygame.draw.rect(self.surface, (255, 0, 0), rect["rect"])

        if self.debug.debug_mode:
            pygame.draw.rect(self.surface, (255, 0, 0), self.player_rect)
            if self.player_left_rect is not None:
                pygame.draw.rect(self.surface, (0, 255, 0), self.player_left_rect)
            if self.player_right_rect is not None:
                pygame.draw.rect(self.surface, (0, 255, 0), self.player_right_rect)
            pygame.draw.rect(self.surface, (0, 255, 0), self.player_down_rect)
        
        self.surface.blit(self.score, (self.surface.get_width() - self.score.get_width() - 10, 10))

        return self.surface
