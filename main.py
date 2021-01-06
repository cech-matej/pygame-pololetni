import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from classes.circle import Circle, okruhy, okruhy_barva
from classes.text import Text, circles
from classes.player import players
from classes.window import window
from components.constants import screen
from components.start import start, start_bool

# import json
from components.open import circles_json

pygame.init()
clock = pygame.time.Clock()

print(okruhy)

circles_num = []
for idx, circle in enumerate(circles_json['circles']):
    circles.append(Circle(circle['x'], circle['y']))
    circles[idx].colour = okruhy_barva[okruhy[idx]]
    if idx > 0:
        circles_num.append(Text('arial', 15, f'{idx}', 'black'))
    else:
        circles_num.append(Text('arial', 15, 'START', 'black'))

pygame.display.set_caption('Hádanka')

running = True
background = pygame.image.load("img/pozadi.jpg")


while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # screen.blit(circle.surf)
    screen.blit(background, (0, 0))

    for i in circles:
        i.update()

    for idx, i in enumerate(circles_num):
        i.update(idx)
        circles_num[0].rect.x -= 5
        screen.blit(i.text_r, i.rect)

    for player in players:
        player.update()
        screen.blit(player.surf, player.rect)

    if window.visibility:
        window.update()

    start()

    clock.tick(40)
    pygame.display.flip()

