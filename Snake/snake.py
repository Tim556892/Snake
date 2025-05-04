CELL_SIZE = 20
WIDTH, HEIGHT = 600, 400

GREEN = (0, 255, 0)

class Snake:
    def __init__(self):
        self._body = [(5, 5)]
        self._direction = (1, 0)
        self._positions_set = set(self._body)

    def move(self):
        head = self._body[0]
        new_head = (head[0] + self._direction[0], head[1] + self._direction[1])
        self._body.insert(0, new_head)
        self._positions_set.add(new_head)

    def set_direction(self, direction):
        self._direction = direction

    def shrink(self):
        tail = self._body.pop()
        self._positions_set.remove(tail)

    def check_collision(self):
        head = self._body[0]
        return (
            head in self._body[1:] or
            head[0] < 0 or head[0] >= WIDTH // CELL_SIZE or
            head[1] < 0 or head[1] >= HEIGHT // CELL_SIZE
        )

    def get_head(self):
        return self._body[0]

    def get_body(self):
        return self._body.copy()

    def get_body_set(self):
        return self._positions_set.copy()

    def get_direction(self):
        return self._direction

    def draw(self, surface):
        import pygame
        for segment in self._body:
            rect = pygame.Rect(
                segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, GREEN, rect)
