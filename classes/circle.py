import pygame
from constants import *


class Circle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Circle, self).__init__()
        self.r = 30
        self.x = x
        self.y = y
        self.colour = (255, 255, 0)
        self.surf = None

    def update(self):
        # Výplň kolečka
        self.surf = pygame.draw.circle(screen, self.colour, (self.x, self.y), self.r, 0)
        # Obrys kolečka
        self.surf = pygame.draw.circle(screen, (0, 0, 0), (self.x, self.y), self.r, 2)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
