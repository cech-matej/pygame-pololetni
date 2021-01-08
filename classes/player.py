import pygame
from pygame.locals import RLEACCEL

from components.constants import screen
from classes.text import circles


class Player(pygame.sprite.Sprite):
    def __init__(self, num, player):
        super(Player, self).__init__()
        self.num = num
        self.surf = pygame.image.load(f"img/player{self.num}.png").convert()

        if player:
            self.surf = pygame.transform.scale(self.surf, (30, 30))
        else:
            self.surf = pygame.transform.scale(self.surf, (100, 100))

        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()

        if not player:
            self.rect.x = 80
            self.rect.y = 80

        self.pos = 0
        self.turn = False

    def update(self):
        if self.num == 1:
            self.rect.x = circles[self.pos].x - 28
            self.rect.y = circles[self.pos].y - 10

        else:
            self.rect.x = circles[self.pos].x - 3
            self.rect.y = circles[self.pos].y - 10


# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player1 = Player(1, True)
player1_window = Player(1, False)
player1.turn = True

player2 = Player(2, True)
player2_window = Player(2, False)

players = pygame.sprite.Group()
players.add(player1, player2)
