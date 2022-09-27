import pygame
import config
from map import world, mini_map, WORLD_WIDTH, WORLD_HEIGHT
import math


class Render:
    def __init__(self, screen, map_screen, clock):
        self.screen=screen
        self.clock=clock
        self.map_screen = map_screen
        self.player_= pygame.transform.scale(pygame.image.load('you.png'), (config.WIDTH/3, config.HEIGHT/3))

        self.f = pygame.transform.scale(pygame.image.load('textures/flor.jpg'), (config.WIDTH, config.HALF_HEIGHT))
        self.bg = pygame.transform.scale(pygame.image.load('textures/bg1.jpg'), (config.WIDTH, config.HALF_HEIGHT))

        #textures
        self.textures = {
        1:pygame.transform.scale(pygame.image.load('textures/wall.jpg').convert(), (config.TEXTURE_WIDTH, config.TEXTURE_HEIGHT)),
        2:pygame.transform.scale(pygame.image.load('textures/wall2.jpg').convert(), (config.TEXTURE_WIDTH, config.TEXTURE_HEIGHT)),
        'E':pygame.transform.scale(pygame.image.load('textures/mist.png').convert(), (config.TEXTURE_WIDTH, config.TEXTURE_HEIGHT))
        }

    def background(self):
        self.screen.blit(self.bg, [0, 0])
        self.screen.blit(self.f, (0, config.HALF_HEIGHT, config.WIDTH, config.HALF_HEIGHT))


    def mini_map_FUNC(self, player_pos, player_angle):
        self.map_screen.fill((160, 160, 160))
        MAP_x, MAP_y = player_pos[0] // config.MAP_SCALE, player_pos[1] // config.MAP_SCALE
        #pygame.draw.line(self.map_screen, (255, 255, 204), (MAP_x, MAP_y), (MAP_x + 10 * math.cos(player_angle), MAP_y + 10 * math.sin(player_angle)), 2)
        #pygame.draw.circle(self.map_screen, (255, 255, 204), (MAP_x, MAP_y), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.map_screen, (18, 18, 18), (x, y, config.MAP_TILE, config.MAP_TILE))
        self.screen.blit(self.map_screen, config.MAP_POSITION)


    def render_info(self, position, player_angle):
        self.screen.blit(self.player_, [config.WIDTH-config.WIDTH/4, config.HEIGHT-config.HEIGHT/2.8])
        if config.info:
                self.screen.blit(pygame.font.Font(None, 30).render('X: '+str(int(position[0]))+ ' Y: '+str(int(position[1])), 3, (0, 0, 0)), (10, config.HEIGHT-20))
                self.screen.blit(pygame.font.Font(None, 30).render('SPEED: '+str(config.SPEED), 3, (0, 0, 0)), (10, config.HEIGHT-45))
                self.screen.blit(pygame.font.Font(None, 30).render('FPS: '+str(int(self.clock.get_fps())), 3, (0, 0, 0)), (10, config.HEIGHT-70))
        self.mini_map_FUNC(position, player_angle)




    def mapping(self, a, b):
        return (a // config.TILE) * config.TILE, (b // config.TILE) * config.TILE


    def ray_casting(self, player):
        walls = list()
        ox, oy = player.position
        xm, ym = self.mapping(ox, oy)
        cur_angle = player.angle - config.HALF_FOV
        for ray in range(config.NUM_RAYS):
            sin_a = math.sin(cur_angle)
            cos_a = math.cos(cur_angle)
            sin_a = sin_a if sin_a else 0.000001
            cos_a = cos_a if cos_a else 0.000001

            # verticals
            x, dx = (xm + config.TILE, 1) if cos_a >= 0 else (xm, -1)
            for i in range(0, WORLD_WIDTH, config.TILE):
                depth_v = (x - ox) / cos_a
                yv = oy + depth_v * sin_a
                tile_v = self.mapping(x + dx, yv)
                if tile_v in world:
                    texture_v = world[tile_v]
                    break
                else:
                    texture_v='E'
                x += dx * config.TILE

            # horizontals
            y, dy = (ym + config.TILE, 1) if sin_a >= 0 else (ym, -1)
            for i in range(0, WORLD_HEIGHT, config.TILE):
                depth_h = (y - oy) / sin_a
                xh = ox + depth_h * cos_a
                tile_h = self.mapping(xh, y + dy)
                if tile_h in world:
                    texture_h = world[tile_h]
                    break
                else:
                    texture_h='E'
                y += dy * config.TILE



            # projection
            depth, offset, texture = (depth_v, yv, texture_v) if depth_v < depth_h else (depth_h, xh, texture_h)
            offset = int(offset) % config.TILE
            depth *= math.cos(player.angle - cur_angle)
            depth * max(depth, 0.00001)
            proj_height = min(int(config.PROJ_COEFF / depth), config.PENTA_HEIGHT)
            wall_column = self.textures[texture].subsurface(offset * config.TEXTURE_SCALE, 0, config.TEXTURE_SCALE, config.TEXTURE_HEIGHT)
            wall_column= pygame.transform.scale(wall_column, (config.SCALE, proj_height))
            wall_position = (ray * config.SCALE, config.HALF_HEIGHT - proj_height // 2)
            walls.append((depth, wall_column, wall_position))
            cur_angle += config.DELTA_ANGLE
        return walls



    def world_render(self, player, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_position = obj
                self.screen.blit(object, object_position)
        self.render_info(player.position, player.angle)









#
