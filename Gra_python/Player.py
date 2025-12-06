import pygame
from screen import *

Player_Width = 20
Player_Height = 60
Player_X = (Width - Player_Width) / 2
Player_Y = (Height - Player_Height) / 2

player_image = pygame.image.load('models/art/characters/player_gun.png')
player_image = pygame.transform.scale(player_image, (Player_Width, Player_Height))

class PLAYER(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,Player_X, Player_Y, Player_Width, Player_Height)
        # self.image = player_image
        self.color = (0, 255, 0)
        self.distance = 5

    def Player_Status(self):
        keys = pygame.key.get_pressed()

        # góra
        if keys[pygame.K_UP]:
            self.y = max(0, self.y - self.distance)

        # dół
        if keys[pygame.K_DOWN]:
            self.y = min(Height - Player_Height, self.y + self.distance)

        # lewo
        if keys[pygame.K_LEFT]:
            self.x = max(0, self.x - self.distance)

        # prawo
        if keys[pygame.K_RIGHT]:
            self.x +=self.distance

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self)