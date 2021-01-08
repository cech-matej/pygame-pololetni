import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN
)

from classes.circle import Circle, okruhy, okruhy_barva
from classes.text import Text, circles
from classes.player import players, player1, player2, player1_window
from classes.window import window

from components.constants import screen, SCREEN_WIDTH, SCREEN_HEIGHT

from components.open import circles_json
from components.open import zemepis_json

import random

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

question = Text('arial', 40, 'a', 'black')
question.rect.y = 200
question.rect.x = 100

pygame.display.set_caption('Hádanka')

start_bool = False
running = True
background = pygame.image.load("img/pozadi.jpg")

# ----------------- START -----------------
start = False

screen.fill((0, 0, 0))
start_text = Text('arial', 50, 'START', 'white')
start_text.rect.x = SCREEN_WIDTH / 2 - 65
start_text.rect.y = SCREEN_HEIGHT / 2 - 30
screen.blit(start_text.text_r, start_text.rect)
pygame.display.flip()

while not start:
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:
            start = True

# ----------------- LOOP -----------------
rep = 0
question_active = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

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

    if player1.turn and rep > 40:
        window.update(1)

        if okruhy[player1.pos] == 0 and question_active:
            i = random.randint(0, len(zemepis_json['otazky']))
            print(zemepis_json['otazky'][i - 1]['otazka'])
            question.text = zemepis_json['otazky'][i - 1]['otazka']
            question.update_question()
            question_active = False

        screen.blit(question.text_r, question.rect)

    clock.tick(40)
    rep += 1
    pygame.display.flip()
