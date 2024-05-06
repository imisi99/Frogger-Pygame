import pygame
from os import walk
from random import choice


class Car(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.name = 'car'

        for _, _, name in walk('../graphics/cars'):
            car_name = choice(name)
        self.image = pygame.image.load('../graphics/cars/' + car_name).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(1, 0)
        self.speed = 300
        self.hitbox = self.rect.inflate(0, -self.rect.height / 2)
        self.initial_pos = pygame.math.Vector2(pos)

        if pos[0] < 200:
            self.direction = pygame.math.Vector2(1, 0)
        else:
            self.direction = pygame.math.Vector2(-1, 0)
            self.image = pygame.transform.flip(self.image, True, False)

    def reset(self):
        self.pos = self.initial_pos
        self.rect.center = self.initial_pos
        self.hitbox.center = self.initial_pos

    def update(self, dt):
        self.pos += self.direction * self.speed * dt
        self.hitbox.center = (round(self.pos.x), round(self.pos.y))
        self.rect.center = self.hitbox.center
        if not -300 < self.rect.x < 3400:
            self.kill()
