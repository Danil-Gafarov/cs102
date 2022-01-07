from copy import deepcopy
from random import choice, randint
from typing import List, Optional, Tuple, Union

import pandas as pd


def create_grid(rows: int = 15, cols: int = 15) -> List[List[Union[str, int]]]:
    return [["■"] * cols for _ in range(rows)]


def remove_wall(
    grid: List[List[Union[str, int]]], coord: Tuple[int, int]
) -> List[List[Union[str, int]]]:
    """

    :param grid:
    :param coord:
    :return:
    """
    direction = choice(("up", "right"))
    if direction == "up":
        if coord[0] != 1:
            grid[coord[0] - 1][coord[1]] = " "
        elif coord[1] + 2 != len(grid[0]):
            grid[coord[0]][coord[1] + 1] = " "
    elif direction == "right":
        if coord[1] + 2 != len(grid[0]):
            grid[coord[0]][coord[1] + 1] = " "
        elif coord[0] != 1:
            grid[coord[0] - 1][coord[1]] = " "
    return grid


def bin_tree_maze(
    rows: int = 15, cols: int = 15, random_exit: bool = True
) -> List[List[Union[str, int]]]:
    """

    :param rows:
    :param cols:
    :param random_exit:
    :return:
    """

    grid = create_grid(rows, cols)
    empty_cells = []
    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if x % 2 == 1 and y % 2 == 1:
                grid[x][y] = " "
                empty_cells.append((x, y))

    for _, cell in enumerate(empty_cells):
        remove_wall(grid, cell)
    # 1. выбрать любую клетку
    # 2. выбрать направление: наверх или направо.
    # Если в выбранном направлении следующая клетка лежит за границами поля,
    # выбрать второе возможное направление
    # 3. перейти в следующую клетку, сносим между клетками стену
    # 4. повторять 2-3 до тех пор, пока не будут пройдены все клетки

    # генерация входа и выхода
    if random_exit:
        x_in, x_out = randint(0, rows - 1), randint(0, rows - 1)
        y_in = randint(0, cols - 1) if x_in in (0, rows - 1) else choice((0, cols - 1))
        y_out = randint(0, cols - 1) if x_out in (0, rows - 1) else choice((0, cols - 1))
    else:
        x_in, y_in = 0, cols - 2
        x_out, y_out = rows - 1, 1

    grid[x_in][y_in], grid[x_out][y_out] = "X", "X"

    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    """
    :param grid:
    :return:
    """
    exits = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "X":
                exits.append((i, j))
    return exits


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """
    :param grid:
    :param k:
    :return:
    """

    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if grid[x][y] != k:
                continue
            if x > 0 and grid[x - 1][y] == 0:
                grid[x - 1][y] = k + 1
            if y > 0 and grid[x][y - 1] == 0:
                grid[x][y - 1] = k + 1
            if x < len(grid) - 1 and grid[x + 1][y] == 0:
                grid[x + 1][y] = k + 1
            if y < len(grid[0]) - 1 and grid[x][y + 1] == 0:
                grid[x][y + 1] = k + 1
    return grid


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """
    :param grid:
    :param exit_coord:
    :return:
    """
    path = [exit_coord]
    x, y = exit_coord[0], exit_coord[1]
    k = int(grid[x][y])
    while k != 1:
        if y != len(grid[0]) - 1 and grid[x][y + 1] == k - 1:
            y += 1
            path.append((x, y))
        if grid[x][y - 1] == k - 1 and y != 0:
            y -= 1
            path.append((x, y))
        if x != len(grid) - 1 and grid[x + 1][y] == k - 1:
            x += 1
            path.append((x, y))
        if grid[x - 1][y] == k - 1 and x != 0:
            x -= 1
            path.append((x, y))

        k -= 1
    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """
    :param grid:
    :param coord:
    :return:
    """
    row, col = len(grid), len(grid[0])
    x, y = coord
    if x == 0 and grid[x + 1][y] != " ":
        return True
    if x == row - 1 and grid[x - 1][y] != " ":
        return True
    if y == 0 and grid[x][y + 1] != " ":
        return True
    if y == col - 1 and grid[x][y - 1] != " ":
        return True

    return False


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """
    :param grid:
    :return:
    """
    origin_grid = deepcopy(grid)
    exits = get_exits(grid)

    if len(exits) == 1:
        return (grid, exits[0])

    if encircled_exit(grid, exits[0]) or encircled_exit(grid, exits[1]):
        return grid, None

    start, finish = exits
    grid[start[0]][start[1]], grid[finish[0]][finish[1]] = 1, 0

    for x, row in enumerate(grid):
        for y, _ in enumerate(row):
            if grid[x][y] == " ":
                grid[x][y] = 0

    k = 1
    while grid[finish[0]][finish[1]] == 0:
        grid = make_step(grid, k)
        k += 1

    path = shortest_path(grid, finish)
    return origin_grid, path


def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
) -> List[List[Union[str, int]]]:
    """
    :param grid:
    :param path:
    :return:
    """

    if path:
        for x, row in enumerate(grid):
            for y, _ in enumerate(row):
                if grid[x][y] != "■":
                    grid[x][y] = " "
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if (i, j) in path:
                    grid[i][j] = "X"
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))
