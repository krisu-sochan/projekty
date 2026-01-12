import pygame
from screen import *

class PLAYER:
    def __init__(self):
        self.x = Width // 2
        self.y = Height // 2

        self.rect = pygame.Rect(self.x, self.y, 60, 80)
        self.attack_rect = pygame.Rect(0, 0, 40, 60)

        # ======================
        # HP
        # ======================
        self.max_hp = 100
        self.hp = self.max_hp
        self.alive = True

        # ======================
        # ATAK
        # ======================
        self.damage = 25
        self.attacking = False
        self.attack_duration = 300   # ms
        self.attack_cooldown = 500   # ms
        self.last_attack_time = 0

        # ======================
        # SPRITY
        # ======================
        self.walk_sheet = pygame.image.load(
            "models/art/characters/Ranger/SMS_Ranger_Walk_2_strip4.png"
        ).convert_alpha()

        self.idle_sheet = pygame.image.load(
            "models/art/characters/Ranger/SMS_Ranger_Idle_1_strip4.png"
        ).convert_alpha()

        self.punch_sheet = pygame.image.load(
            "models/art/characters/Ranger/SMS_Ranger_Punch_2.png"
        ).convert_alpha()

        self.animations = {
            "walk": self.load_strip(self.walk_sheet),
            "idle": self.load_strip(self.idle_sheet),
            "punch": [pygame.transform.scale(self.punch_sheet, (80, 80))]

        }

        self.state = "idle"
        self.frame = 0
        self.anim_speed = 0.15
        self.image = self.animations["idle"][0]

        # ======================
        # RUCH
        # ======================
        self.speed = 3
        self.facing_left = False

    def load_strip(self, sheet):
        frames = []
        for i in range(4):
            frame = sheet.subsurface((i * 16, 0, 16, 32))
            frame = pygame.transform.scale(frame, (80, 80))
            frames.append(frame)
        return frames

    def update(self):
        if not self.alive:
            return

        keys = pygame.key.get_pressed()
        now = pygame.time.get_ticks()
        moving = False

        # ======================
        # RUCH
        # ======================
        if not self.attacking:
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
        # ATAK
        # ======================
        if keys[pygame.K_SPACE]:
            if not self.attacking and now - self.last_attack_time > self.attack_cooldown:
                self.attacking = True
                self.attack_start_time = now
                self.last_attack_time = now
                self.state = "punch"
                self.frame = 0

        if self.attacking:
            if now - self.attack_start_time > self.attack_duration:
                self.attacking = False

        # ======================
        # STATE
        # ======================
        if self.attacking:
            self.state = "punch"
        else:
            self.state = "walk" if moving else "idle"

        # ======================
        # RECTY
        # ======================
        self.rect.topleft = (self.x, self.y)

        if self.facing_left:
            self.attack_rect.topleft = (self.x - 40, self.y + 10)
        else:
            self.attack_rect.topleft = (self.x + 60, self.y + 10)

        self.animate()

    def animate(self):
        frames = self.animations[self.state]
        self.frame += self.anim_speed

        if self.frame >= len(frames):
            self.frame = 0

        image = frames[int(self.frame)]
        if self.facing_left:
            image = pygame.transform.flip(image, True, False)
        self.image = image

    def take_damage(self, amount):
        if not self.alive:
            return

        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.alive = False

    def draw(self, screen, scroll):
        if not self.alive:
            return

        # HP BAR
        pygame.draw.rect(screen, (255, 0, 0), (20, 20, self.max_hp * 3, 20))
        pygame.draw.rect(screen, (0, 255, 0), (20, 20, self.hp * 3, 20))

        screen.blit(self.image, (self.x - scroll, self.y))


