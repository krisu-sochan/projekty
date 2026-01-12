import pygame
import random
from sys import exit

from screen import *
from Player import PLAYER
from enemy import ENEMY
from map import Map

# ======================
# INIT
# ======================
pygame.init()
screen = pygame.display.set_mode(Res)
# icon="models/art/characters/Ranger/SMS_Ranger_Title_Screen.png"
pygame.display.set_caption("Beat 'em up")

clock = pygame.time.Clock()

# ======================
# OBIEKTY
# ======================
player = PLAYER()
game_map = Map()

# ======================
# ENEMY SPAWN (RAZ)
# ======================
enemies = []

SPAWN_DISTANCE = 600
START_X = 600
END_X = game_map.bar_x

for x in range(START_X, END_X, SPAWN_DISTANCE):
    enemies.append(ENEMY(x, Height - random.randint(160,220)))

# ======================
# KAMERA
# ======================
scroll = 0

def update_camera(player, game_map):
    global scroll

    scroll = player.x - Width // 2

    if scroll < 0:
        scroll = 0

    if scroll > game_map.width - Width:
        scroll = game_map.width - Width

# ======================
# GAME LOOP
# ======================
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # ======================
    # UPDATE
    # ======================
    player.update()
    update_camera(player, game_map)

    for enemy in enemies:
        enemy.update(player)

        if player.attacking and player.attack_rect.colliderect(enemy.rect):
            enemy.take_damage(player.damage)
    # ======================
    # DRAW
    # ======================
    screen.fill((0, 0, 0))

    game_map.draw(screen, scroll)
    player.draw(screen, scroll)

    for enemy in enemies:
        enemy.draw(screen, scroll)

    pygame.display.update()
    clock.tick(60)
