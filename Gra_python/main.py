import pygame
from sys import exit
from Player import PLAYER
from screen import *

pygame.init()

# screen
screen = pygame.display.set_mode(Res)
pygame.display.set_caption("Beat them up")
clock = pygame.time.Clock()

# background
background = pygame.image.load(
    "models/art/backgrounds/street-background.png"
).convert()
background = pygame.transform.scale(background, (Width, Height))

player = PLAYER()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0, 0))

    player.update()
    player.draw(screen)

    pygame.display.update()
    clock.tick(60)
