import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
clock = pygame.time.Clock()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 900


class Circle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Circle, self).__init__()
        self.r = 30
        self.x = x
        self.y = y
        self.colour = (255, 255, 0)
        self.surf = None

    def update(self):
        self.surf = pygame.draw.circle(screen, self.colour, (self.x, self.y), self.r, 0)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hádanka')

running = True
background = pygame.image.load("img/pozadi.jpg")

circle = [Circle(10, 10), Circle(1000, 800)]

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    # screen.blit(circle.surf)
    screen.blit(background, (0, 0))

    for i in circle:
        i.update()
    clock.tick(40)
    pygame.display.flip()

