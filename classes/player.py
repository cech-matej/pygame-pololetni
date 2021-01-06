import pygame
from pygame.locals import RLEACCEL

from components.constants import screen
from classes.text import circles


class Player(pygame.sprite.Sprite):
    def __init__(self, num):
        super(Player, self).__init__()
        self.num = num
        self.surf = pygame.image.load(f"img/player{self.num}.png").convert()
        self.surf = pygame.transform.scale(self.surf, (30, 30))
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
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

player1 = Player(1)
player1.turn = True
player2 = Player(2)

players = pygame.sprite.Group()
players.add(player1, player2)
