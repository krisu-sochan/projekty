import pygame
from screen import *

def camera():
    scroll=0
    background = pygame.image.load(
        "models/art/backgrounds/street-background.png"
    ).convert()
    background = pygame.transform.scale(background, (Width, Height))
    bg_width = background.get_width()
    koniec_poziomu=3500
    print(bg_width)
