import pygame
import random

RED = (255,0,0)
WIDTH = 800
HEIGHT = 700

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface([20,20])
        pygame.draw.rect(self.image, RED, [0,0,20,20])
        self.rect = self.image.get_rect()

        self.velocity = [random.randint(3,7),random.randint(4,8)]
    
    def initialPos(self):
        self.rect.x = (WIDTH/2) - 10
        self.rect.y = HEIGHT - 300

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounceX(self):
        self.velocity[0] = -self.velocity[0]

    def bounceY(self):
        self.velocity[1] = -self.velocity[1]