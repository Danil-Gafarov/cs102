import pathlib
import random
import typing as tp
from copy import deepcopy
from pprint import pprint as pp

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        self.rows, self.cols = size
        self.prev_generation = [[0]]
        self.curr_generation = self.create_grid(randomize=randomize)
        self.max_gens = max_generations
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        grid = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(random.randint(0, 1) if randomize else 0)
            grid.append(row)
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        neighbours = []
        x, y = cell[0], cell[1]
        if x >= 1:
            neighbours.append(self.curr_generation[x - 1][y])
        if x + 1 < self.rows:
            neighbours.append(self.curr_generation[x + 1][y])
        if y >= 1:
            neighbours.append(self.curr_generation[x][y - 1])
        if y + 1 < self.cols:
            neighbours.append(self.curr_generation[x][y + 1])
        if x >= 1 and y >= 1:
            neighbours.append(self.curr_generation[x - 1][y - 1])
        if x >= 1 and y + 1 < self.cols:
            neighbours.append(self.curr_generation[x - 1][y + 1])
        if x + 1 < self.rows and y >= 1:
            neighbours.append(self.curr_generation[x + 1][y - 1])
        if x + 1 < self.rows and y + 1 < self.cols:
            neighbours.append(self.curr_generation[x + 1][y + 1])
        return neighbours

    def get_next_generation(self) -> Grid:
        new_generation = []
        for x in range(0, self.rows, 1):
            row = []
            for y in range(0, self.cols, 1):

                neighbours_sum = sum(self.get_neighbours((x, y)))
                if neighbours_sum == 3:
                    row.append(1)
                elif neighbours_sum == 2 and self.curr_generation[x][y] == 1:
                    row.append(1)
                else:
                    row.append(0)
            new_generation.append(row)
        return new_generation

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        if self.is_changing and not self.is_max_generations_exceeded:
            self.prev_generation = deepcopy(self.curr_generation)
            self.curr_generation = self.get_next_generation()
            self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        if self.max_gens:
            return self.generations >= self.max_gens
        else:
            return False

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        if self.curr_generation != self.prev_generation:
            return True
        else:
            return False

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        current = []
        with open(filename, "r", encoding="utf-8") as input_grid:
            for line in input_grid:
                if len(line) > 1:
                    current.append(list(map(int, line[0:-1])))
        life = GameOfLife((len(current), len(current[0])))
        life.curr_generation = current
        return life

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename, "w", encoding="utf-8") as output_grid:
            for i, rows in enumerate(self.curr_generation):
                for j, elem in enumerate(rows):
                    output_grid.write(str(elem))
                output_grid.write("\n")


if __name__ == "__main__":
    life = GameOfLife.from_file(pathlib.Path("glider.txt"))
    pp(life.curr_generation)
    for _ in range(4):
        pp(life.prev_generation)
        pp(life.curr_generation)
        life.step()
