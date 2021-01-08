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


class WindowOdpoved(Window):
    def __init__(self):
        super(WindowOdpoved, self).__init__()
        self.colour = (217, 217, 217)

    def update(self, cislo):
        self.surf = pygame.draw.rect(screen, self.colour, (200, 330+cislo*105, 800, 95), border_radius=50)
        self.surf = pygame.draw.rect(screen, "black", (200, 330+cislo*105, 800, 95), 2, border_radius=50)


window = Window()
w_odp1 = WindowOdpoved()
w_odp2 = WindowOdpoved()
w_odp3 = WindowOdpoved()
w_odp4 = WindowOdpoved()
w_odpovedi = pygame.sprite.Group(w_odp1, w_odp2, w_odp3, w_odp4)
