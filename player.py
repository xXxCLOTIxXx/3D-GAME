import pygame
import config
import math
from map import collision

class Player:
    def __init__(self, sprites):
        self.x, self.y = config.POSITION
        self.angle=config.ANGLE
        self.sens = config.mouse_sensor
        self.side = 50
        self.rect = pygame.Rect(*config.POSITION, self.side, self.side)
        self.sprites = sprites
        self.sprite_collision = [pygame.Rect(*obj.position, obj.side, obj.side) for obj in
            self.sprites.objects_list if obj.collision]
        self.collision_list = collision + self.sprite_collision

    def collision_detect(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_inds = next_rect.collidelistall(self.collision_list)

        if len(hit_inds):
            delta_x, delta_y = 0, 0
            for hit_ind in hit_inds:
                hit_rect = self.collision_list[hit_ind]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top
            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        self.x += dx
        self.y += dy
    def move(self, world):
        self.keys_move(world)
        self.mouse()
        self.rect.center = self.x, self.y
        self.angle %=config.DOUBLE_PI

    def keys_move(self, world):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys=pygame.key.get_pressed()
        if (self.x, self.y) in world:return
        if keys[pygame.K_CAPSLOCK]:config.SPEED = 2
        else:config.SPEED = 4
        if keys[pygame.K_w]:
            if keys[pygame.K_LSHIFT]:config.SPEED = 8
            dx = config.SPEED * cos_a
            dy = config.SPEED * sin_a
            self.collision_detect(dx, dy)
        elif keys[pygame.K_s]:
            dx = -config.SPEED * cos_a
            dy = -config.SPEED * sin_a
            self.collision_detect(dx, dy)
        if keys[pygame.K_a]:
            dx = config.SPEED * sin_a
            dy = -config.SPEED * cos_a
            self.collision_detect(dx, dy)
        elif keys[pygame.K_d]:
            dx = -config.SPEED * sin_a
            dy = config.SPEED * cos_a
            self.collision_detect(dx, dy)


    def mouse(self):
        if pygame.mouse.get_focused():
            dif = pygame.mouse.get_pos()[0] - config.HALF_WIDTH
            pygame.mouse.set_pos((config.HALF_WIDTH, config.HALF_HEIGHT))
            self.angle += dif * self.sens


    @property
    def position(self):
        return (self.x, self.y)
