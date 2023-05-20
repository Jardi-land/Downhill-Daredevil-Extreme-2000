# ------------------
# Author: Lorenzo De Zen / Nathan Marchand
# License: Check the LICENSE file
# ------------------

import pygame  # Import de la librairie pygame
from pygame import mixer

import alias as al


class Camera:
    """Représente la caméra pour afficher le jeu dans une fenêtre.

    Attributes:
        player_image (pygame.Surface): L'image du joueur.
        player_spawn_pos (tuple): La position de départ du joueur, spécifiée en tant que tuple (x, y).
        player_rect (pygame.Rect): Le rectangle englobant du joueur.
        
    Methods:
        calc_vector_offset(): Calcule le décalage vectoriel pour le rendu des chunks.
        draw(chunk_list): Dessine les éléments du jeu sur la surface de la caméra et renvoie cette surface.

    Example:
        camera = Camera(player_image=my_player_image, player_spawn_pos=(100, 200), player_rect=my_player_rect)
        camera.draw(chunk_list=my_chunk_list)
    """
    def __init__(self, player_image, player_spawn_pos, player_rect, player_track) -> None:
        from debug import Debug_overlay
        self.debug = Debug_overlay
        self.surface = pygame.Surface((1920, 1080)).convert_alpha()
        self.player_image = player_image
        self.player_pos = pygame.math.Vector2(player_spawn_pos[0], player_spawn_pos[1])
        self.player_rect = player_rect
        self.player_status = "alive"
        
        self.player_track = player_track
        self.surface_track = pygame.Surface((1920, self.player_pos.y - self.player_image.get_height()/2)).convert_alpha()
        self.surface_track.fill((0, 0, 0, 0))
        self.surface_track_full = pygame.Surface((1920, self.player_pos.y - self.player_image.get_height()/2)).convert_alpha()
        self.surface_track_full.fill((0, 0, 0, 0))
        
        self.bonus_hit = False
        
        mixer.init()
        
        self.hit_sound = mixer.Sound(al.path("files/sound/hit.mp3"))
        self.powerup = mixer.Sound(al.path("files/sound/powerup.mp3"))
        
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
        
        #<-- Track zone -->
        #Blit track static on player
        self.surface.blit(self.player_track, (self.player_pos.x - self.player_image.get_width()/2, self.player_pos.y - self.player_image.get_height()/2))
        #Get track moving surface_track
        self.surface_track.blit(self.player_track, (self.player_pos.x - self.player_image.get_width()/2, self.player_pos.y - self.player_image.get_height()/2 - self.player_speed))
        #Copy full track and blit higher
        self.surface_track_full_copy = self.surface_track_full.copy()
        self.surface_track_full.fill((0, 0, 0, 0))
        self.surface_track_full.blit(self.surface_track_full_copy, (0, -self.player_speed))
        #Blit moving track on full track
        self.surface_track_full.blit(self.surface_track, (0, 0))
        #Clear moving track
        self.surface_track.fill((0, 0, 0, 0))
        #Blit full track on camera surface
        self.surface.blit(self.surface_track_full, (0, 0))
        #<-- Track zone -->
        
        
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
                if chunk.bonus:
                    chunk.speed_minus_rect.x = chunk.speed_minus_pos[0] + self.vector_offset.x
                    chunk.speed_minus_rect.y = chunk.speed_minus_pos[1] + (self.vector_offset.y + (value*chunk.surfaces["up"].get_height()))
                    if self.player_rect.colliderect(chunk.speed_minus_rect):
                        self.bonus_hit = True
                        chunk.bonus = False
                        mixer.Sound.play(self.powerup)
                    if self.debug.debug_mode:
                        pygame.draw.rect(self.surface, (0, 255, 0), chunk.speed_minus_rect)

        if self.debug.debug_mode:
            pygame.draw.rect(self.surface, (255, 0, 0), self.player_rect)
        
        self.surface.blit(self.score, (self.surface.get_width() - self.score.get_width() - 10, 10))

        return self.surface
