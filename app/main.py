import pygame
import sys
from settings import *
from player import Player

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Frogger")
clock = pygame.time.Clock()

pygame.init()

all_sprite = pygame.sprite.Group()
player = Player((500, 500), all_sprite)

while True:

    dt = clock.tick(120) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill("black")

    all_sprite.update(dt)

    all_sprite.draw(display_surface)

    pygame.display.update()
