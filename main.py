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
from classes.window import window, w_odpovedi

from components.constants import screen, SCREEN_WIDTH, SCREEN_HEIGHT

from components.open import circles_json
from components.open import zemepis_json
from components.otazka import blit_otazky, blit_odpoved
from components.buttons import button_pos
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
odpoved1 = Text('arial', 20, 'a', 'black')
odpoved2 = Text('arial', 20, 'a', 'black')
odpoved3 = Text('arial', 20, 'a', 'black')
odpoved4 = Text('arial', 20, 'a', 'black')
odpovedi = pygame.sprite.Group(odpoved1, odpoved2, odpoved3, odpoved4)
question.rect.y = 200
question.rect.x = 100
odpoved1.rect.y = 365
odpoved1.rect.x = 300
odpoved2.rect.y = 470
odpoved2.rect.x = 300
odpoved3.rect.y = 575
odpoved3.rect.x = 300
odpoved4.rect.y = 680
odpoved4.rect.x = 300

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
rand_otaz = 0
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
            rand_otaz = random.randint(0, len(zemepis_json['otazky']))

            question.text = blit_otazky(rand_otaz)
            question.update_question()

            for idx, odpoved in enumerate(odpovedi):
                odpoved.text = blit_odpoved(rand_otaz, idx+1)
                odpoved.update_question()
            question_active = False
        for idx, btn in enumerate(w_odpovedi):
            btn.update(idx)
        for textik in odpovedi:
            screen.blit(textik.text_r, textik.rect)
        screen.blit(question.text_r, question.rect)
        save_click = zemepis_json['otazky'][rand_otaz - 1]['check']
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] >= button_pos['x'] \
                        and pygame.mouse.get_pos()[1] >= button_pos['y']+(save_click-1)*button_pos['k']:
                    if pygame.mouse.get_pos()[0] <= button_pos['posun_x']+button_pos['x']\
                            and pygame.mouse.get_pos()[1] <= button_pos['posun_y']+button_pos['y']\
                            + (save_click-1) * button_pos['k']:
                        print("Spravne!")
                else:
                    print("Špatně!")
    clock.tick(40)
    rep += 1
    pygame.display.flip()
