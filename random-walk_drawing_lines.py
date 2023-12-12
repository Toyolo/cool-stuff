import pygame
import random


pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

class Walker:
    def __init__(self) -> None:
        self.x = screen.get_width() // 2
        self.y = screen.get_height() // 2
        self.trail = []  # Store positions and colors

    def draw(self):
        for pos, color in self.trail:
            pygame.draw.circle(screen, color, pos, 5)

    def move(self, steps):
        for _ in range(steps):
            self.x += random.choice([-5, 5])
            self.y += random.choice([-5, 5])
            self.color = (0, random.randint(0, 255), random.randint(0, 255))
            self.trail.append(((self.x, self.y), self.color))

walker = Walker()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    walker.draw()
    walker.move(10)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
