import pygame
import sys
import random

class SnakeGame:
    def __init__(self):
        self.size = (800, 600)
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = [(200, 200), (220, 200), (240, 200)]
        self.direction = (20, 0)
        self.apple = self.get_random_apple()

    def get_random_apple(self):
        return (random.randint(0, 39) * 20, random.randint(0, 29) * 20)

    def draw_snake(self):
        for pos in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(pos[0], pos[1], 20, 20))

    def draw_apple(self):
        pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.apple[0], self.apple[1], 20, 20))

    def move_snake(self):
        new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])
        self.snake.insert(0, new_head)
        if self.snake[0] == self.apple:
            self.apple = self.get_random_apple()
        else:
            self.snake.pop()

    def check_collision(self):
        if (self.snake[0][0] < 0 or self.snake[0][0] >= self.size[0] or
            self.snake[0][1] < 0 or self.snake[0][1] >= self.size[1]):
            return True
        for pos in self.snake[1:]:
            if self.snake[0] == pos:
                return True
        return False

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and self.direction != (0, 20):
                        self.direction = (0, -20)
                    elif event.key == pygame.K_DOWN and self.direction != (0, -20):
                        self.direction = (0, 20)
                    elif event.key == pygame.K_LEFT and self.direction != (20, 0):
                        self.direction = (-20, 0)
                    elif event.key == pygame.K_RIGHT and self.direction != (-20, 0):
                        self.direction = (20, 0)

            self.move_snake()
            if self.check_collision():
                break

            self.screen.fill((0, 0, 0))
            self.draw_snake()
            self.draw_apple()
            pygame.display.flip()
            self.clock.tick(10)

        pygame.quit()
        sys.exit()