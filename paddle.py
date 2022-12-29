import pygame

BLACK = (0,0,0)
WIDTH = 800
HEIGHT = 700

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([120,20])
        pygame.draw.rect(self.image, BLACK,[0,0,120,20])
        self.rect = self.image.get_rect()

    def moveRight(self):
        self.rect.x += 6
        if self.rect.x >= (WIDTH - 120):
            self.rect.x = WIDTH - 120

    def moveLeft(self):
        self.rect.x -= 6
        if self.rect.x <= 0:
            self.rect.x = 0
