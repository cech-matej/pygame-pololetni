import pygame
from components.constants import SCREEN_WIDTH, SCREEN_HEIGHT, screen
from classes.text import Text

start_bool = False


def start():
    s = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    s.set_alpha(200)
    s.fill((255, 255, 255))
    screen.blit(s, (0, 0))

    pygame.draw.rect(screen, (0, 0, 0), (SCREEN_WIDTH/2 - 150, SCREEN_HEIGHT/2 - 50, 300, 100), border_radius=10)

    start_text = Text('arial', 50, 'START', 'white')
    start_text.rect.x = SCREEN_WIDTH/2 - 65
    start_text.rect.y = SCREEN_HEIGHT/2 - 30
    screen.blit(start_text.text_r, start_text.rect)
