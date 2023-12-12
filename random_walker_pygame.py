import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

class Walker:
    def __init__(self) -> None:
        self.x = screen.get_width() // 2
        self.y = screen.get_height() // 2
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = 10
        self.prev_x = self.x
        self.prev_y = self.y

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

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
            self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Changes color randomly careful if you got epilepsy

walker = Walker()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    walker.draw()
    walker.move(10)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()