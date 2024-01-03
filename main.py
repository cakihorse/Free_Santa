import sys

from tkinter.messagebox import showinfo
import pygame

from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800, 500))

level = [
    " WWWWWWWWWWWWWWWWWWWWW ",
    " W                   W",
    " W             WWWWW W",
    " W      WWWW       W W",
    " W   W          WWWW W ",
    " W WWW  WWWW         W ",
    " W   W     W W       W ",
    " W   WWW WWW        WW ",
    " W   WWW     WWW W W W ",
    " W      W W      W W W ",
    " WWW W       WWWWW W W ",
    " W W      WW         W ",
    " W W WWWW        WWW W ",
    " W W         E   W   W ",
    " WWWWWWWWWWWWWWWWWWWWW ",
]

walls = []
end_rect = None
loose_rect = None
win = pygame.image.load("res/win.png")
loose = pygame.image.load("res/loose.png")
clock = pygame.time.Clock()
FPS = 60
paused = pygame.image.load("res/paused.png")


class Wall:
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 32, 32)


class Game:
    def __init__(self):
        self.player = Player()
        self.pressed = {}


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
        for wall in walls:
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


game = Game()
player = Player()

pygame.display.set_caption('Free Santa !')
while True:
    clock.tick(60)


    def easterEgg():
        showinfo("Easter Egg:", "Bravo tu as trouvé la touche secrete :) !")


    x = 0
    y = 0
    for row in level:
        for col in row:
            if col == "W":
                Wall((x, y))
                loose_rect = pygame.Rect(x, y, 32, 32)
            if col == "E":
                end_rect = pygame.Rect(x, y, 32, 32)
            x += 32
        y += 32
        x = 0

        if game.pressed.get(pygame.K_LEFT):
            player.move(-2, 0)
        elif game.pressed.get(pygame.K_RIGHT):
            player.move(2, 0)
        elif game.pressed.get(pygame.K_DOWN):
            player.move(0, 2)
        elif game.pressed.get(pygame.K_UP):
            player.move(0, -2)

    # check if the window is closed.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            if event.key == pygame.K_m:
                print("Easter Egg : Hi ! I'm an easter Egg !")
                easterEgg()
                
            elif event.key == pygame.K_ESCAPE:
                screen.blit(paused, (0, 0))
                pygame.display.flip()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

    for wall in walls:
        pygame.draw.rect(screen, (255, 255, 255), wall.rect)

    if player.rect.colliderect(end_rect):
        screen.fill((0, 0, 0))
        screen.blit(win, (0, 0))
        pygame.display.flip()
    elif player.rect.colliderect(loose_rect):
        screen.blit(loose, (0, 0))
        pygame.display.flip()

    player.draw(screen)
    pygame.display.update()
