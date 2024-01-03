import main
import pygame

class Wall:
    def __init__(self, pos):
        main.walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)

