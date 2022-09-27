import pygame
import config
from player import Player
import math
from map import world
from time import sleep as s
from render import Render
from os import system as sy
from objects import Sprite

class Game:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((config.WIDTH, config.HEIGHT))
        self.map_screen=pygame.Surface(config.MINI_MAP_RES)
        pygame.display.set_caption('3D WALKER 1.6')
        self.clock = pygame.time.Clock()
        pygame.mouse.set_visible(False)
        self.sprites = Sprite()
        self.player=Player(self.sprites)
        self.render=Render(self.screen, self.map_screen, self.clock)
        sy('cls || clear')

    def start(self):
        self.screen.fill((191, 191, 191))
        self.screen.blit(pygame.font.Font(None, 60).render('F10 - EXIT', 3, (0, 0, 0)), (230, 90))
        self.screen.blit(pygame.font.Font(None, 60).render('F3 -   show info', 3, (0, 0, 0)), (230, 130))
        self.screen.blit(pygame.font.Font(None, 60).render('   W', 3, (0, 0, 0)), (230, 175))
        self.screen.blit(pygame.font.Font(None, 60).render('A S D -   movement', 3, (0, 0, 0)), (230, 210))
        self.screen.blit(pygame.font.Font(None, 60).render('CAPSLOCK -   slow walking', 3, (0, 0, 0)), (230, 250))
        self.screen.blit(pygame.font.Font(None, 60).render('L SHIFT -   run', 3, (0, 0, 0)), (230, 290))
        pygame.display.update()
        s(4)




    def main(self):
        self.start()
        while config.game:
            keys=pygame.key.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    config.game=False
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if keys[pygame.K_F3]:
                        if config.info:config.info=False
                        else:config.info=True

            if keys[pygame.K_F10]:
                    config.game=False
                    pygame.quit()

            self.player.move(world)
            self.screen.fill((0, 0, 0))
            self.render.background()
            walls = self.render.ray_casting(self.player)
            self.render.world_render(player=self.player, world_objects=walls + [obj.locate(self.player, walls) for obj in self.sprites.objects_list])
            pygame.display.flip()
            self.clock.tick(config.FPS)
if __name__ == '__main__':
    client=Game()
    client.main()
