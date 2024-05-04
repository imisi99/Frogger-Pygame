import pygame


class SimpleSpriteClass(pygame.sprite.Sprite):
    def __init__(self, surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -self.rect.height / 2)


class LongSpriteClass(pygame.sprite.Sprite):
    def __init__(self, surf, pos, group):
        super().__init__(group)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-self.rect.width * 0.8, -self.rect.height / 2)
        self.hitbox.bottom = self.rect.bottom - 10
