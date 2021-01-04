import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

from classes.circle import Circle
from classes.text import Text, circles
from constants import *

import json

pygame.init()
clock = pygame.time.Clock()

with open('json/circle_pos.json') as f:
    circles_json = json.load(f)

# circles = []
circles_num = []
for idx, circle in enumerate(circles_json['circles']):
    circles.append(Circle(circle['x'], circle['y']))
    circles_num.append(Text('arial', 15, f'{idx}', 'black'))

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hádanka')

running = True
background = pygame.image.load("img/pozadi.jpg")

# circles = [Circle(50, 790), Circle(1000, 800)]

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
        screen.blit(i.text_r, i.rect)

    clock.tick(40)
    pygame.display.flip()

