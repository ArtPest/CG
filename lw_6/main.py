import pygame
from settings import *
from player import Player
import math
from map import world_map
from drawing import Drawing

pygame.init()
pygame.mixer.init()

sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player()
drawing = Drawing(sc)

pygame.mixer.music.load('audio/darklabirynth.wav')
pygame.mixer.music.play(-1)

footstep_sound = pygame.mixer.Sound('audio/footstep_echoed.wav')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player_speed_before = player.speed
    player.movement()

    if player.speed > 0 and player_speed_before == 0:
        footstep_sound.play(-1)
    elif player.speed == 0 and player_speed_before > 0:
        footstep_sound.stop()

    sc.fill((0, 0, 0))
    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)

    pygame.display.flip()
    clock.tick()
