import random
from snake import CELL_SIZE, WIDTH, HEIGHT

RED = (255, 0, 0)

class Fruit:
    def __init__(self):
        self._position = (0, 0)

    def respawn(self, forbidden_positions):
        while True:
            position = (
                random.randint(0, (WIDTH // CELL_SIZE) - 1),
                random.randint(0, (HEIGHT // CELL_SIZE) - 1)
            )
            if position not in forbidden_positions:
                self._position = position
                break

    def get_position(self):
        return self._position

    def draw(self, surface):
        import pygame
        rect = pygame.Rect(
            self._position[0] * CELL_SIZE,
            self._position[1] * CELL_SIZE,
            CELL_SIZE,
            CELL_SIZE
        )
        pygame.draw.rect(surface, RED, rect)
