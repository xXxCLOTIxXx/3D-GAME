import config
import pygame
_ = None

map =[
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,_,_,_,_,_,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,_,_,_,2,2,_,_,_,_,_],
[1,_,2,_,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,_,_,_,_,2,2,_,2,2,2,_,2,_,_,2,1,1,1],
[1,_,2,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,_,_,_,_,2,_,2,_,_,2,_,2,2,_,2,_,_,1],
[1,_,2,2,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,_,_,_,_,_,_,2,2,_,_,_,_,_,_,2,_,_,1],
[1,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,_,2,2,2,2,_,_,2,2,2,2,2,2,_,_,_,_,1],
[1,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,_,2,_,_,2,2,_,_,_,_,_,_,2,2,2,2,_,1],
[1,_,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,_,2,_,_,_,_,2,2,2,2,2,2,2,_,_,_,_,1],
[1,_,2,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,_,2,_,_,_,_,_,_,_,_,_,_,2,_,_,_,_,1],
[1,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,_,2,2,2,_,_,_,_,_,_,_,_,2,_,2,2,2,1],
[1,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,_,_,_,2,_,_,_,_,_,_,_,_,2,_,2,_,_,1],
[1,_,2,2,2,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,2,2,2,2,_,_,_,_,_,_,_,_,2,_,_,2,_,1],
[1,_,_,_,_,2,2,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,_,2,_,1],
[1,_,2,2,_,_,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,2,2,2,2,_,2,_,1],
[1,_,_,_,2,2,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,_,_,_,_,_,2,_,1],
[1,2,2,_,_,2,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,_,2,2,2,2,2,_,1],
[1,_,2,_,_,2,_,2,2,2,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,_,2,_,_,_,_,_,1],
[1,_,2,_,_,2,_,2,_,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,_,2,_,2,2,2,_,1],
[1,_,2,2,2,2,_,2,_,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,2,_,2,_,2,_,2,_,1],
[1,_,_,_,_,_,_,2,_,2,2,2,2,2,2,2,_,_,_,_,_,_,_,_,_,_,_,_,2,2,2,_,2,_,2,_,2,_,1],
[1,_,2,_,2,_,2,2,_,_,_,_,_,_,_,2,_,_,_,_,_,_,_,_,_,_,_,_,2,_,_,_,2,_,_,_,_,_,1],
[1,_,2,_,2,_,2,2,2,2,_,2,2,2,_,2,_,_,_,_,_,_,_,2,2,2,2,2,2,_,2,2,2,_,2,2,2,_,1],
[1,_,2,_,2,_,_,_,_,_,_,2,_,2,_,2,_,_,_,_,_,_,_,2,_,_,_,_,_,_,2,_,_,_,_,_,2,_,1],
[1,2,2,_,2,_,2,2,2,2,2,2,_,2,_,2,2,2,2,2,2,2,2,2,_,2,2,2,2,2,2,2,2,2,2,2,2,_,1],
[1,_,_,_,2,_,_,_,_,_,_,_,_,2,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,_,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

WORLD_WIDTH = len(map[0]) * config.TILE
WORLD_HEIGHT = len(map) * config.TILE
world = {}
mini_map = set()
collision = list()
for j, row in enumerate(map):
    for i, char in enumerate(row):
        if char:
            mini_map.add((i * config.MAP_TILE, j * config.MAP_TILE))
            collision.append(pygame.Rect(i * config.TILE, j * config.TILE, config.TILE, config.TILE))
            if char == 1:
                world[(i * config.TILE, j * config.TILE)] = 1
            elif char == 2:
                world[(i * config.TILE, j * config.TILE)] = 2
