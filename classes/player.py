import pygame
from pygame.locals import RLEACCEL

from components.constants import screen, SCREEN_WIDTH, SCREEN_HEIGHT
from classes.text import circles, Text


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


player1 = Player(1, True)
player1_window = Player(1, False)
player1.turn = True

player2 = Player(2, True)
player2_window = Player(2, False)

players = pygame.sprite.Group()
players.add(player1, player2)


def switch_turn():
    if player1.turn:
        player1.turn = False
        player2.turn = True
    else:
        player1.turn = True
        player2.turn = False


def is_end():
    if player1.pos == 18:
        screen.fill((30, 144, 255))
        end = Text('arial', 50, 'Vyhrál MODRÝ hráč!', 'white')
        end.rect.x = SCREEN_WIDTH / 2 - 240
        end.rect.y = SCREEN_HEIGHT / 2 - 25
        screen.blit(end.text_r, end.rect)
        return True
    elif player2.pos == 18:
        screen.fill((204, 0, 0))
        end = Text('arial', 50, 'Vyhrál ČERVENÝ hráč!', 'white')
        end.rect.x = SCREEN_WIDTH / 2 - 260
        end.rect.y = SCREEN_HEIGHT / 2 - 25
        screen.blit(end.text_r, end.rect)
        return True

    return False
