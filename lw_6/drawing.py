import pygame
from settings import *
from ray_casting import ray_casting

class Drawing:
    def __init__(self, sc):
        self.sc = sc
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = {
            'space': pygame.image.load('images/open_space.png').convert()
        }

    def background(self):
        screen_width, screen_height = self.sc.get_size()
        space_width, space_height = self.textures['space'].get_size()

        for x in range(0, screen_width, space_width):
            for y in range(0, screen_height, space_height):
                self.sc.blit(self.textures['space'], (x, y))

    def world(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, (128,128,128))
        self.sc.blit(render, FPS_POS)
