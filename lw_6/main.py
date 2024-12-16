import pygame
from settings import *
from player import Player
import math
from map import world_map
from drawing import Drawing

# Инициализация Pygame и звука
pygame.init()
pygame.mixer.init()

# Настройки экрана и времени
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Игрок и рисование
player = Player()
drawing = Drawing(sc)

# Загрузка фоновой музыки и звуков шагов
pygame.mixer.music.load('audio/darklabirynth.wav')
pygame.mixer.music.play(-1)  # -1 для зацикливания

footstep_sound = pygame.mixer.Sound('audio/footstep_echoed.wav')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Движение игрока и шаги
    player_speed_before = player.speed
    player.movement()

    # Воспроизведение шагов, если игрок движется
    if player.speed > 0 and player_speed_before == 0:  # Игрок начал двигаться
        footstep_sound.play(-1)  # Зацикливаем шаги
    elif player.speed == 0 and player_speed_before > 0:  # Игрок остановился
        footstep_sound.stop()

    # Очистка экрана и рендеринг
    sc.fill((0, 0, 0))
    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)

    pygame.display.flip()
    clock.tick()
