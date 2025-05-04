import pygame
from abc import ABC, abstractmethod


class MoveStrategy(ABC):
    @abstractmethod
    def get_direction(self, current_direction, snake=None, fruit=None):
        pass


class KeyboardMoveStrategy(MoveStrategy):
    def get_direction(self, current_direction, snake=None, fruit=None):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and current_direction != (0, 1):
            return (0, -1)
        if keys[pygame.K_DOWN] and current_direction != (0, -1):
            return (0, 1)
        if keys[pygame.K_LEFT] and current_direction != (1, 0):
            return (-1, 0)
        if keys[pygame.K_RIGHT] and current_direction != (-1, 0):
            return (1, 0)
        return current_direction


class AIMoveStrategy(MoveStrategy):
    def get_direction(self, current_direction, snake=None, fruit=None):
        if snake is None or fruit is None:
            return current_direction  # fail-safe fallback

        head_x, head_y = snake.get_head()
        fruit_x, fruit_y = fruit.get_position()

        dx = fruit_x - head_x
        dy = fruit_y - head_y

        if abs(dx) > abs(dy):
            if dx > 0 and current_direction != (-1, 0):
                return (1, 0)
            elif dx < 0 and current_direction != (1, 0):
                return (-1, 0)
        if dy > 0 and current_direction != (0, -1):
            return (0, 1)
        elif dy < 0 and current_direction != (0, 1):
            return (0, -1)

        return current_direction
