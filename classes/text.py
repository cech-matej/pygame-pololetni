import pygame


class Text(pygame.sprite.Sprite):
    def __init__(self, font, size, text, color):
        super(Text, self).__init__()
        self.font = font
        self.size = size
        self.text = text
        self.color = color

        txt = pygame.font.SysFont(self.font, self.size)
        self.text_r = txt.render(self.text, True, self.color)
        self.rect = self.text_r.get_rect()

    def update(self, num):
        self.rect.x = circles[num].x - 15
        self.rect.y = circles[num].y - 25


circles = []
