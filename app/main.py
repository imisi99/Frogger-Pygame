import pygame
import sys
from settings import *
from player import Player
from cars import Car
from random import choice, randint
from sprite import SimpleSpriteClass, LongSpriteClass


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
obstacle_sprite = pygame.sprite.Group()
player = Player((2062, 3274), all_sprite, obstacle_sprite)

car_timer = pygame.event.custom_type()
pygame.time.set_timer(car_timer, 50)
pos_list = []

for file_name, pos_list in SIMPLE_OBJECTS.items():
    path = f'../graphics/objects/simple/{file_name}.png'
    surf = pygame.image.load(path).convert_alpha()
    for pos in pos_list:
        SimpleSpriteClass(surf, pos, [all_sprite, obstacle_sprite])

for file_name, pos_list in LONG_OBJECTS.items():
    path = f'../graphics/objects/long/{file_name}.png'
    surf = pygame.image.load(path).convert_alpha()
    for pos in pos_list:
        LongSpriteClass(surf, pos, [all_sprite, obstacle_sprite])

music = pygame.mixer.Sound('../audio/music.mp3')
music.play(-1)

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
                car = Car(random_pos, [all_sprite, obstacle_sprite])
            if len(pos_list) > 5:
                del pos_list[0]

    if player.life >= 0:
        if player.rect.centery >= 1180:
            all_sprite.update(dt)

            all_sprite.custom_draw()

        if player.rect.centery < 1180:
            display_surface.fill("blue")
            font = pygame.font.Font('../graphics/subatomic.ttf', 20)
            text_fail = font.render("Congratulations You Won Press P to play again or Q to quit the game!", True, (200, 200, 200))
            text_fail_rect = text_fail.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2)))
            display_surface.blit(text_fail, text_fail_rect)
            pygame.draw.rect(display_surface, "green", text_fail_rect.inflate(50, 30), width=7, border_radius=5)
            keys = pygame.key.get_pressed()

            if keys[pygame.K_p]:
                player.pos = (2062, 3274)
                player.life = 3
            elif keys[pygame.K_q]:
                pygame.quit()
                sys.exit()

    if player.life < 0:
        display_surface.fill("blue")
        font = pygame.font.Font('../graphics/subatomic.ttf', 20)
        text_fail = font.render("You lose Press P to play again or Q to quit the game", True, (200, 200, 200))
        text_fail_rect = text_fail.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2)))
        display_surface.blit(text_fail, text_fail_rect)
        pygame.draw.rect(display_surface, "green", text_fail_rect.inflate(50, 30), width=7, border_radius=5)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_p]:
            player.pos = (2062, 3274)
            player.life = 3
        elif keys[pygame.K_q]:
            pygame.quit()
            sys.exit()

    pygame.display.update()
