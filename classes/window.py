import pygame
from components.constants import screen


class Window(pygame.sprite.Sprite):
    def __init__(self):
        super(Window, self).__init__()
        self.colour = (255, 255, 255)
        self.surf = None
        self.visibility = False

    def update(self):
        # Výplň kolečka
        self.surf = pygame.draw.rect(screen, self.colour, (50, 50, 1100, 800), border_radius=50)
        # Obrys kolečka
        self.surf = pygame.draw.rect(screen, (0, 0, 0), (50, 50, 1100, 800), 2, border_radius=50)


window = Window()
