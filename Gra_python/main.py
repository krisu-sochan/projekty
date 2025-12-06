import pygame
from sys import exit
from Player import *
from screen import *

pygame.init()

# images
backgrounds_image = pygame.image.load('models/art/backgrounds/street-background.png')
backgrounds_image = pygame.transform.scale(backgrounds_image, (Width, Height))

# screen setup
screen = pygame.display.set_mode(Res)
pygame.display.set_caption("Beat them up")
icon = pygame.image.load('models/art/ui/go-go-go.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

player = PLAYER()

def draw():
    screen.fill((20, 18, 167))
    screen.blit(backgrounds_image, (0, 0))

    # zamiast obrazu — prostokąt gracza
    player.draw(screen)

def update():
    pygame.display.update()
    clock.tick(60)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    player.Player_Status()
    draw()
    update()
