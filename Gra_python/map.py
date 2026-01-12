import pygame
from screen import *
class Map:
    def __init__(self):
        self.background = pygame.image.load(
            "models/art/backgrounds/street-background.png"
        ).convert_alpha()

        self.background = pygame.transform.scale(
            self.background, (Width * 3, Height)
        )

        self.background_bar = pygame.image.load(
            "models/art/backgrounds/bar-entrance.png"
        ).convert_alpha()

        self.bar_width = Width // 2
        self.background_bar = pygame.transform.scale(
            self.background_bar, (self.bar_width, Height)
        )

        self.width = self.background.get_width()

        # 🔹 światowa pozycja baru (koniec mapy)
        self.bar_x = self.width - self.bar_width

    def draw(self, screen, scroll):
        screen.blit(self.background, (-scroll, 0))

        # 🔹 rysuj bar tylko gdy jest w kamerze
        if scroll + Width > self.bar_x:
            screen.blit(self.background_bar, (self.bar_x - scroll, 0))

