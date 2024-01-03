import pygame
import main

class Player:

    def __init__(self):

        self.rect = pygame.Rect(64, 64, 32, 32)
        self.sprite = pygame.image.load("res/santa_top.png")
        self.sprite = pygame.transform.scale(self.sprite, (32, 32))

    def draw(self, screen):
        screen.blit(self.sprite, self.rect)

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        for wall in main.walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy < 0:
                    self.rect.top = self.rect.bottom
                if dy > 0:
                    self.rect.bottom = self.rect.top

        new_sprite = "left"
        if dx > 0:
            new_sprite = "right"
        elif dx < 0:
            new_sprite = "left"
        elif dy > 0:
            new_sprite = "bottom"
        elif dy < 0:
            new_sprite = "top"
        self.change_animation(new_sprite)

    def change_animation(self, dir):
        self.sprite = pygame.image.load("res/santa_" + dir + ".png")
        self.sprite = pygame.transform.scale(self.sprite, (32, 32))