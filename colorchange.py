import pygame
import random

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

class Box(pygame.sprite.Sprite):
    def __init__(self, color, pos):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)

    def change_color(self):
        self.image.fill((random.randint(0,255), random.randint(0,255), random.randint(0,255)))

box1 = Box((255, 0, 0), (100, 150))
box2 = Box((0, 0, 255), (300, 150))
all_sprites = pygame.sprite.Group(box1, box2)

CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 1000)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            for sprite in all_sprites:
                sprite.change_color()

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
