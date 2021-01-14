import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    MOUSEBUTTONDOWN
)

from classes.circle import Circle, okruhy, okruhy_barva
from classes.text import Text, circles
from classes.player import players, player1, player2, switch_turn, is_end
from classes.window import window, w_odpovedi, button_order, window_clear

from components.constants import screen, SCREEN_WIDTH, SCREEN_HEIGHT, TIMER

from components.open import circles_json
from components.open import zemepis_json, dejepis_json, literatura_json
from components.otazka import blit_otazky, blit_odpoved
from components.buttons import button_pos
from components.output_pdf import q_player1, q_player2, a_player1, a_player2, c_player1, c_player2, output

import random


def active_question(pos, p_list):
    rand, save = None, None
    if okruhy[pos] == 0:
        rand = random.randint(0, len(zemepis_json['otazky']))
        save = zemepis_json['otazky'][rand - 1]['check']
        p_list.append(zemepis_json['otazky'][rand - 1]['otazka'])
    elif okruhy[pos] == 1:
        rand = random.randint(0, len(dejepis_json['otazky']))
        save = dejepis_json['otazky'][rand - 1]['check']
        p_list.append(dejepis_json['otazky'][rand - 1]['otazka'])
    elif okruhy[pos] == 2:
        rand = random.randint(0, len(literatura_json['otazky']))
        save = literatura_json['otazky'][rand - 1]['check']
        p_list.append(literatura_json['otazky'][rand - 1]['otazka'])

    return rand, save


def q_a_update(okruh):
    question.text = blit_otazky(rand_otaz, okruh)
    question.update_question()

    for index, odpoved in enumerate(odpovedi):
        odpoved.text = blit_odpoved(rand_otaz, index + 1, okruh)
        odpoved.update_question()


def btn_txt_update():
    for index, btn in enumerate(w_odpovedi):
        btn.update(index)

    for textik in odpovedi:
        screen.blit(textik.text_r, textik.rect)
    screen.blit(question.text_r, question.rect)
    spatne_kontrola[save_click - 1] = 0


def answer_check(active_player):
    m_x, m_y = pygame.mouse.get_pos()
    # Správně
    if m_x >= button_pos['x'] and m_y >= button_pos['y'] + (save_click - 1) * button_pos['k']:
        if m_x <= button_pos['posun_x'] + button_pos['x'] and m_y <= button_pos['posun_y'] + button_pos['y'] \
                + (save_click - 1) * button_pos['k']:
            button_order[save_click - 1].colour = (50, 205, 50)
            if active_player == 1:
                player1.pos += 1

                output_append(a_player1, save_click)
                c_player1.append(1)
            else:
                player2.pos += 1

                output_append(a_player2, save_click)
                c_player2.append(1)

            switch_turn()
    # Špatně
    for index, number in enumerate(spatne_kontrola):
        if number == 1:
            if m_x >= button_pos['x'] and m_y >= button_pos['y'] + index * button_pos['k']:
                if m_x <= button_pos['posun_x'] + button_pos['x'] and m_y <= button_pos['posun_y'] + button_pos['y'] \
                        + index * button_pos['k']:
                    button_order[index].colour = (255, 0,  0)

                    if active_player == 1:
                        output_append(a_player1, index + 1)
                        c_player1.append(0)
                    else:
                        output_append(a_player2, index + 1)
                        c_player2.append(0)

                    switch_turn()
    btn_txt_update()
    window_clear()

    pygame.display.flip()
    pygame.time.wait(2000)


def output_append(p_list, number):
    if number == 1:
        p_list.append(odpoved1.text)
    elif number == 2:
        p_list.append(odpoved2.text)
    elif number == 3:
        p_list.append(odpoved3.text)
    elif number == 4:
        p_list.append(odpoved4.text)


pygame.init()
clock = pygame.time.Clock()

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

mouse_down = False
spatne_kontrola = [1, 1, 1, 1]
save_click = None

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            mouse_down = True
        else:
            mouse_down = False

    screen.blit(background, (0, 0))

    for i in circles:
        i.update()

    for idx, i in enumerate(circles_num):
        i.update(idx)
        circles_num[0].rect.x -= 5
        screen.blit(i.text_r, i.rect)
    if not is_end():
        for player in players:
            player.update()
            screen.blit(player.surf, player.rect)

        # <-------- Kontrola odpovědi -------->
        # Hráč 1
        if player1.turn and rep > TIMER:
            window.update(1)

            if question_active:
                rand_otaz, save_click = active_question(player1.pos, q_player1)

                q_a_update(okruhy[player1.pos])
                question_active = False

            btn_txt_update()

            if mouse_down:
                question_active = True
                answer_check(1)
                rep = 0

        # Hráč 2
        if player2.turn and rep > TIMER:
            window.update(2)

            if question_active:
                rand_otaz, save_click = active_question(player2.pos, q_player2)

                q_a_update(okruhy[player2.pos])
                question_active = False

            btn_txt_update()

            if mouse_down:
                question_active = True
                answer_check(2)
                rep = 0
        spatne_kontrola = [1, 1, 1, 1]
    clock.tick(40)
    rep += 1
    pygame.display.flip()


output(1, q_player1, a_player1, c_player1)
output(2, q_player2, a_player2, c_player2)
