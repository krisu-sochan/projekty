import pygame

class ENEMY:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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
        # AI / RUCH
        # ======================
        self.speed = 2
        self.attack_range = 60
        self.facing_left = True

        # ======================
        # HP
        # ======================
        self.max_hp = 50
        self.hp = self.max_hp
        self.alive = True

        # ======================
        # ATAK
        # ======================
        self.damage = 10
        self.attack_cooldown = 1000
        self.attack_duration = 300
        self.last_attack_time = 0
        self.attacking = False
        self.attack_start_time = 0

        self.rect = pygame.Rect(self.x, self.y, 60, 80)

    def load_strip(self, sheet):
        frames = []
        for i in range(4):
            frame = sheet.subsurface((i * 16, 0, 16, 32))
            frame = pygame.transform.scale(frame, (80, 80))
            frames.append(frame)
        return frames

    def take_damage(self, amount):
        if not self.alive:
            return
        self.hp -= amount
        if self.hp <= 0:
            self.hp = 0
            self.alive = False

    def update(self, player):
        if not self.alive:
            return

        now = pygame.time.get_ticks()

        # ======================
        # ATAK – trwa
        # ======================
        if self.attacking:
            if now - self.attack_start_time > self.attack_duration:
                self.attacking = False
            self.state = "punch"
        else:
            self.ai_move(player)

        # ======================
        # RECT
        # ======================
        self.rect.topleft = (self.x, self.y)

        # ======================
        # PRÓBA ATAKU
        # ======================
        self.try_attack(player, now)

        self.animate()

    def ai_move(self, player):
        dx = player.x - self.x
        dy = player.y - self.y

        if abs(dx) > self.attack_range:
            self.state = "walk"
            self.x += self.speed if dx > 0 else -self.speed
            self.facing_left = dx < 0
        else:
            self.state = "idle"

        if abs(dy) > 5:
            self.y += 1 if dy > 0 else -1

    def try_attack(self, player, now):
        if (
            not self.attacking
            and self.rect.colliderect(player.rect)
            and now - self.last_attack_time > self.attack_cooldown
        ):
            self.attacking = True
            self.attack_start_time = now
            self.last_attack_time = now
            self.state = "punch"
            player.take_damage(self.damage)

    def animate(self):
        frames = self.animations[self.state]
        self.frame += self.anim_speed
        if self.frame >= len(frames):
            self.frame = 0

        image = frames[int(self.frame)]
        if self.facing_left:
            image = pygame.transform.flip(image, True, False)
        self.image = image

    def draw(self, screen, scroll):
        if not self.alive:
            return
        screen.blit(self.image, (self.x - scroll, self.y))
