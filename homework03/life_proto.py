import random
import typing as tp

import pygame

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self, width: int = 640, height: int = 480, cell_size: int = 10, speed: int = 2
    ) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.screen_size = width, height
        self.screen = pygame.display.set_mode(self.screen_size)
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size
        self.speed = speed
        self.grid = self.create_grid(randomize=True)

    def draw_lines(self) -> None:
        """Отрисовать сетку"""
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color("black"), (0, y), (self.width, y))

    def run(self) -> None:
        """Запустить игру"""
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption("Game of Life")
        self.screen.fill(pygame.Color("white"))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw_grid()
            self.draw_lines()
            self.grid = self.get_next_generation()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def create_grid(self, randomize: bool = False) -> Grid:
        """
        Создание списка клеток.

        Клетка считается живой, если ее значение равно 1, в противном случае клетка
        считается мертвой, то есть, ее значение равно 0.

        Parameters
        ----------
        randomize : bool
            Если значение истина, то создается матрица, где каждая клетка может
            быть равновероятно живой или мертвой, иначе все клетки создаются мертвыми.

        Returns
        ----------
        out : Grid
            Матрица клеток размером `cell_height` х `cell_width`.
        """

        grid = []
        for i in range(self.cell_height):
            row = []
            for j in range(self.cell_width):
                row.append(random.randint(0, 1) if randomize else 0)
            grid.append(row)
        return grid

    def draw_grid(self) -> None:
        """
        Отрисовка списка клеток с закрашиванием их в соответствующе цвета.
        """
        for y in range(0, self.height // self.cell_size, 1):
            for x in range(0, self.width // self.cell_size, 1):
                color = pygame.Color("white" if self.grid[y][x] == 0 else "green")
                x_coord = x * self.cell_size
                y_coord = y * self.cell_size
                pygame.draw.rect(
                    self.screen, color, (x_coord, y_coord, self.cell_size, self.cell_size)
                )

    def get_neighbours(self, cell: Cell) -> Cells:
        """
        Вернуть список соседних клеток для клетки `cell`.

        Соседними считаются клетки по горизонтали, вертикали и диагоналям,
        то есть, во всех направлениях.

        Parameters
        ----------
        cell : Cell
            Клетка, для которой необходимо получить список соседей. Клетка
            представлена кортежем, содержащим ее координаты на игровом поле.

        Returns
        ----------
        out : Cells
            Список соседних клеток.
        """
        neighbours = []
        x = cell[0] // self.cell_size
        y = cell[1] // self.cell_size
        if x >= 1:
            neighbours.append(self.grid[x - 1][y])
        if x + 1 < self.cell_height:
            neighbours.append(self.grid[x + 1][y])
        if y >= 1:
            neighbours.append(self.grid[x][y - 1])
        if y + 1 < self.cell_width:
            neighbours.append(self.grid[x][y + 1])
        if x >= 1 and y >= 1:
            neighbours.append(self.grid[x - 1][y - 1])
        if x >= 1 and y + 1 < self.cell_width:
            neighbours.append(self.grid[x - 1][y + 1])
        if x + 1 < self.cell_height and y >= 1:
            neighbours.append(self.grid[x + 1][y - 1])
        if x + 1 < self.cell_height and y + 1 < self.cell_width:
            neighbours.append(self.grid[x + 1][y + 1])
        return neighbours

    def get_next_generation(self) -> Grid:
        """
        Получить следующее поколение клеток.

        Returns
        ----------
        out : Grid
            Новое поколение клеток.
        """
        new_generation = []
        for x in range(0, self.height // self.cell_size, 1):
            row = []
            for y in range(0, self.width // self.cell_size, 1):
                x_coord = x * self.cell_size
                y_coord = y * self.cell_size
                neighbours_sum = sum(self.get_neighbours((x_coord, y_coord)))
                if neighbours_sum == 3:
                    row.append(1)
                elif neighbours_sum == 2 and self.grid[x][y] == 1:
                    row.append(1)
                else:
                    row.append(0)
            new_generation.append(row)
        return new_generation


if __name__ == "__main__":
    game = GameOfLife(720, 480, 80)
    game.run()
