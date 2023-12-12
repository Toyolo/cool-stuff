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
            choice = random.randint(0, 7)
            self.prev_x = self.x
            self.prev_y = self.y
            if choice == 0:
                self.x += 1
            elif choice == 1:
                self.x -= 1
            elif choice == 2:
                self.y += 1
            elif choice == 3:
                self.y -= 1
            elif choice == 4:
                self.x += 1
                self.y += 1
            elif choice == 5:
                self.x += 1
                self.y -= 1
            elif choice == 6:
                self.x -= 1
                self.y += 1
            elif choice == 7:
                self.x -= 1
                self.y -= 1
            self.color = (random.randint(0, 150), random.randint(0,200), random.randint(0, 100))
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
