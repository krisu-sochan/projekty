import pygame
from screen import *

class PLAYER:
    def __init__(self):
        # ======================
        # POZYCJA
        # ======================
        self.x = Width // 2
        self.y = Height // 2

        # ======================
        # WCZYTYWANIE SPRITE’ÓW
        # ======================
        self.walk_sheet = pygame.image.load(
            "models/art/characters/Ranger/SMS_Ranger_Walk_2_strip4.png"
        ).convert_alpha()

        self.idle_sheet = pygame.image.load(
            "models/art/characters/Ranger/SMS_Ranger_Idle_1_strip4.png"
        ).convert_alpha()

        # ======================
        # ANIMACJE
        # ======================
        self.animations = {
            "walk": self.load_strip(self.walk_sheet),
            "idle": self.load_strip(self.idle_sheet)
        }

        # ======================
        # STAN
        # ======================
        self.state = "idle"
        self.frame = 0
        self.anim_speed = 0.15
        self.image = self.animations["idle"][0]

        # ======================
        # RUCH
        # ======================
        self.speed = 3
        self.facing_left = False

    # ======================
    # ŁADOWANIE KLATEK
    # ======================
    def load_strip(self, sheet):
        frames = []
        for i in range(4):
            frame = sheet.subsurface((i * 16, 0, 16, 32))
            frame = pygame.transform.scale(frame, (64, 64))
            frames.append(frame)
        return frames

    # ======================
    # UPDATE
    # ======================
    def update(self):
        keys = pygame.key.get_pressed()
        moving = False

        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.facing_left = True
            moving = True
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.facing_left = False
            moving = True
        if keys[pygame.K_UP]:
            self.y -= self.speed
            moving = True
        if keys[pygame.K_DOWN]:
            self.y += self.speed
            moving = True

        # ======================
        # ZMIANA STANU
        # ======================
        self.state = "walk" if moving else "idle"

        self.animate()

    # ======================
    # ANIMACJA
    # ======================
    def animate(self):
        frames = self.animations[self.state]

        self.frame += self.anim_speed
        if self.frame >= len(frames):
            self.frame = 0

        image = frames[int(self.frame)]

        if self.facing_left:
            image = pygame.transform.flip(image, True, False)

        self.image = image

    # ======================
    # RYSOWANIE
    # ======================
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
