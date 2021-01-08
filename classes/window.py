import pygame
from components.constants import screen
from classes.player import player1_window, player2_window


class Window(pygame.sprite.Sprite):
    def __init__(self):
        super(Window, self).__init__()
        self.colour = (255, 255, 255)
        self.surf = None
        self.visibility = False

    def update(self, player):
        # Výplň
        self.surf = pygame.draw.rect(screen, self.colour, (50, 50, 1100, 800), border_radius=50)
        # Obrys
        self.surf = pygame.draw.rect(screen, (0, 0, 0), (50, 50, 1100, 800), 2, border_radius=50)

        if player == 1:
            screen.blit(player1_window.surf, player1_window.rect)
        else:
            screen.blit(player2_window.surf, player2_window.rect)


window = Window()
