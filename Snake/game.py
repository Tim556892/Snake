import pygame
import os
import sys

from snake import Snake, WIDTH, HEIGHT
from fruit import Fruit
from strategies import KeyboardMoveStrategy

SPEED = 10
BLACK = (0, 0, 0)
SCORES_FILE = 'scores.txt'
MAX_SCORES = 100


class Game:
    def __init__(self):
        pygame.init()
        self._screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake")
        self._clock = pygame.time.Clock()
        self._snake = Snake()
        self._fruit = Fruit()
        self._strategy = KeyboardMoveStrategy()
        self._running = True
        self._score = 0
        self._highscore = self._load_highscore()
        self._fruit.respawn(self._snake.get_body_set())

    def _load_highscore(self):
        if not os.path.exists(SCORES_FILE):
            return 0
        with open(SCORES_FILE, 'r') as file:
            scores = [int(line.strip())
                      for line in file if line.strip().isdigit()]
            return max(scores) if scores else 0

    def _save_score(self):
        with open(SCORES_FILE, 'a') as file:
            file.write(f"{self._score}\n")

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False

    def _update(self):
        direction = self._strategy.get_direction(
            self._snake.get_direction(), self._snake, self._fruit
        )

        self._snake.set_direction(direction)
        self._snake.move()

        if self._snake.check_collision():
            self._save_score()
            self._running = False

        if self._snake.get_head() == self._fruit.get_position():
            self._score += 1
            self._fruit.respawn(self._snake.get_body_set())
        else:
            self._snake.shrink()

    def _draw_text(self, text, position, size=24, color=(255, 255, 255)):
        font = pygame.font.SysFont(None, size)
        surface = font.render(text, True, color)
        self._screen.blit(surface, position)

    def _draw(self):
        self._screen.fill(BLACK)
        self._fruit.draw(self._screen)
        self._snake.draw(self._screen)
        self._draw_text(f"Score: {self._score}", (10, 10))
        self._draw_text(f"Highscore: {self._highscore}", (10, 40))
        pygame.display.flip()

    def run(self):
        while self._running:
            self._clock.tick(SPEED)
            self._handle_events()
            self._update()
            self._draw()
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Game().run()
