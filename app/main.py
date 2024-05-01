import pygame
import sys
from settings import *
from player import Player
from cars import Car
from random import choice, randint


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.offset = pygame.math.Vector2(0, 0)
        self.bg = pygame.image.load('../graphics/main/map.png').convert()
        self.fg = pygame.image.load('../graphics/main/overlay.png').convert_alpha()

    def custom_draw(self):
        self.offset.x = player.rect.centerx - WINDOW_WIDTH / 2
        self.offset.y = player.rect.centery - WINDOW_HEIGHT / 2

        display_surface.blit(self.bg, -self.offset)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            display_surface.blit(sprite.image, offset_pos)

        display_surface.blit(self.fg, -self.offset)


display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()

pygame.init()

all_sprite = AllSprites()
player = Player((500, 500), all_sprite)

car_timer = pygame.event.custom_type()
pygame.time.set_timer(car_timer, 50)
pos_list = []
while True:

    dt = clock.tick(120) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == car_timer:
            random_pos = choice(CAR_START_POSITIONS)
            if random_pos not in pos_list:
                pos_list.append(random_pos)
                pos = (random_pos[0], random_pos[1] + randint(-8, 8))
                car = Car(random_pos, all_sprite)
            if len(pos_list) > 5:
                del pos_list[0]

    display_surface.fill("black")

    all_sprite.update(dt)

    # all_sprite.draw(display_surface)
    all_sprite.custom_draw()

    pygame.display.update()
