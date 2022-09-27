import pygame
import config
import math
from collections import deque

class Sprite:
    def __init__(self):
        self.sprite_parameters = {
            'sprite':{
                'sprite': pygame.image.load('textures/sprites/sprite.png').convert_alpha(),
                'static':True,
                'shift': 1.8,
                'scale': 0.4,
                'animation': False,
                'anim_dist': None,
                'anim_speed': None,
                'collision': False,
            }
        }
        self.objects_list=[
            #SpriteObjects(self.sprite_parameters['sprite'], (7.1, 2.1))
        ]




class SpriteObjects:
    def __init__(self, sprite_parameters, pos):
        self.object = sprite_parameters['sprite']
        self.static = sprite_parameters['static']
        self.x, self.y = pos[0] * config.TILE, pos[1] * config.TILE
        self.shift = sprite_parameters['shift']
        self.scale = sprite_parameters['scale']
        self.animation = sprite_parameters['animation']
        self.collision=sprite_parameters['collision']
        self.side = 30
        self.position = self.x - self.side // 2, self.y - self.side // 2
        if self.animation:
            self.anim_dist=sprite_parameters['anim_dist']
            self.anim_speed=sprite_parameters['anim_speed']
            self.anim_count = 0

        if not self.static:
            self.sprite_angles = [frozenset(range(i, i + 45)) for i in range(0, 360, 45)]
            self.sprite_position = {angle: position for angle, position in zip(self.sprite_angles, self.object)}

    def locate(self, player, walls):
        dx, dy = self.x - player.x, self.y - player.y
        distance_sptite = math.sqrt(dx**2 + dy**2)
        theta = math.atan2(dy, dx)
        gamma = theta - player.angle
        if dx > 0 and 180 <= math.degrees(player.angle) <= 360 or dx < 0 and dy < 0:
            gamma += config.DOUBLE_PI
        delta_rays = int(gamma / config.DELTA_ANGLE)
        current_ray = config.CENTER_RAY + delta_rays
        distance_sptite *= math.cos(config.HALF_FOV - current_ray * config.DELTA_ANGLE)
        fake_ray = current_ray + config.FAKE_RAYS
        if 0 <= fake_ray <= config.FAKE_RAYS_RANGE and  distance_sptite > 30:
            proj_height = min(int(config.PROJ_COEFF / distance_sptite * self.scale), config.DOUBLE_HEIGHT)
            half_proj_height = proj_height // 2
            shift = half_proj_height * self.shift

            if not self.static:
                if theta <0:
                    theta+=config.DOUBLE_PI
                theta = 360 - int(math.degrees(theta))
                for angles in self.sprite_angles:
                    if theta in angles:
                        self.object = self.sprite_position[angles]
                        break
            #anim
            sprite_obj = self.object
            if self.animation:
                if distance_sptite < self.anim_dist:
                    sprite_obj = self.animation[0]
                    if self.anim_count < self.anim_speed:
                        self.anim_count+=1
                    else:
                        self.animation.rotate()
                        anim_count = 0


            sprite_position = (current_ray * config.SCALE - half_proj_height, config.HALF_HEIGHT - half_proj_height + shift)
            sprite = pygame.transform.scale(sprite_obj, (proj_height, proj_height))
            return (distance_sptite, sprite, sprite_position)
        else:
            return (False,)








#
