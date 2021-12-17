from random import choice
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
    cols = len(grid[0])
    i, j = coord[0], coord[1]
    if i - 2 < 0:
        if j + 2 < cols:
            grid[i][j + 1] = " "
    elif j + 2 >= cols:
        grid[i - 1][j] = " "
    else:
        rnd = choice([0, 1])
        if rnd == 0:
            grid[i][j + 1] = " "
        else:
            grid[i - 1][j] = " "
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
    for i in range(1, rows, 2):
        for j in range(1, cols, 2):
            remove_wall(grid, (i, j))
    if random_exit:
        possible_cells = (
            [[i, 0] for i in range(1, rows, 2)]
            + [[i, cols - 1] for i in range(1, rows, 2)]
            + [[0, i] for i in range(1, cols, 2)]
            + [[rows - 1, i] for i in range(1, cols, 2)]
        )
        possible_cells += [[0, 0], [rows - 1, 0], [0, cols - 1], [rows - 1, cols - 1]]
        x_start, y_start = choice(possible_cells)
        x_exit, y_exit = choice(possible_cells)
    else:
        x_start, y_start = 0, cols - 1
        x_exit, y_exit = rows - 1, 0

    grid[x_start][y_start] = "X"
    grid[x_exit][y_exit] = "X"

    return grid


def get_exits(grid: List[List[Union[str, int]]]) -> List[Tuple[int, int]]:
    """
    :param grid:
    :return:
    """
    rows = len(grid)
    cols = len(grid[0])
    exits = []
    for i in range(cols):
        if grid[0][i] == "X":
            if (0, i) not in exits:
                exits.append((0, i))
        if grid[rows - 1][i] == "X":
            if (rows - 1, i) not in exits:
                exits.append((rows - 1, i))
    for i in range(rows):
        if grid[i][0] == "X":
            if (i, 0) not in exits:
                exits.append((i, 0))
        if grid[i][cols - 1] == "X":
            if (i, cols - 1) not in exits:
                exits.append((i, cols - 1))
    return sorted(exits)


def make_step(grid: List[List[Union[str, int]]], k: int) -> List[List[Union[str, int]]]:
    """
    :param grid:
    :param k:
    :return:
    """
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == k:
                if i - 1 >= 0:
                    if grid[i - 1][j] == 0:
                        grid[i - 1][j] = k + 1
                if i + 1 < rows:
                    if grid[i + 1][j] == 0:
                        grid[i + 1][j] = k + 1
                if j - 1 >= 0:
                    if grid[i][j - 1] == 0:
                        grid[i][j - 1] = k + 1
                if j + 1 < cols:
                    if grid[i][j + 1] == 0:
                        grid[i][j + 1] = k + 1
    return grid


def shortest_path(
    grid: List[List[Union[str, int]]], exit_coord: Tuple[int, int]
) -> Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]:
    """
    :param grid:
    :param exit_coord:
    :return:
    """
    path = []
    rows = len(grid)
    cols = len(grid[0])
    k = int(grid[exit_coord[0]][exit_coord[1]])
    while k != 1:
        i, j = exit_coord[0], exit_coord[1]
        path.append((i, j))
        if i - 1 >= 0:
            if grid[i - 1][j] == k - 1:
                k -= 1
                exit_coord = (i - 1, j)
        if i + 1 < rows:
            if grid[i + 1][j] == k - 1:
                k -= 1
                exit_coord = (i + 1, j)
        if j - 1 >= 0:
            if grid[i][j - 1] == k - 1:
                k -= 1
                exit_coord = (i, j - 1)
        if j + 1 < cols:
            if grid[i][j + 1] == k - 1:
                k -= 1
                exit_coord = (i, j + 1)
    path.append((exit_coord[0], exit_coord[1]))
    return path


def encircled_exit(grid: List[List[Union[str, int]]], coord: Tuple[int, int]) -> bool:
    """
    :param grid:
    :param coord:
    :return:
    """
    pass


def solve_maze(
    grid: List[List[Union[str, int]]],
) -> Tuple[List[List[Union[str, int]]], Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]]:
    """
    :param grid:
    :return:
    """

    exits = get_exits(grid)
    if len(exits) == 1:
        return grid, [exits[0]]
    #  if encircled_exit(grid, exits[0]) or encircled_exit(grid, exits[1]):
    #  return None, None
    rows = len(grid)
    cols = len(grid[0])
    start, exit = exits[0], exits[1]
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] != "■":
                grid[i][j] = 0
    start_cell = (start[0], start[1])
    exit_cell = (exit[0], exit[1])
    #  отдельно рассмотрим угловые двери
    if start[0] == 0:
        if start[1] == 0:
            start_cell = (1, 1)
        elif start[1] == cols - 1:
            start_cell = (1, cols - 2)
    elif start[0] == rows - 1:
        if start[1] == 0:
            start_cell = (rows - 2, 1)
        elif start[1] == cols - 1:
            start_cell == (rows - 2, cols - 2)
    if exit[0] == 0:
        if exit[1] == 0:
            exit_cell = (1, 1)
        elif exit[1] == cols - 1:
            exit_cell = (1, cols - 2)
    elif exit[0] == rows - 1:
        if exit[1] == 0:
            exit_cell = (rows - 2, 1)
        elif exit[1] == cols - 1:
            exit_cell = (rows - 2, cols - 2)
    grid[start_cell[0]][start_cell[1]] = 1
    grid[exit_cell[0]][exit_cell[1]] = 0
    k = 0
    while grid[exit_cell[0]][exit_cell[1]] == 0:
        k += 1
        make_step(grid, k)
    path = shortest_path(grid, exit_cell)
    return grid, path


def add_path_to_grid(
    grid: List[List[Union[str, int]]], path: Optional[Union[Tuple[int, int], List[Tuple[int, int]]]]
) -> List[List[Union[str, int]]]:
    """
    :param grid:
    :param path:
    :return:
    """

    if path:
        for i, row in enumerate(grid):
            for j, _ in enumerate(row):
                if (i, j) in path:
                    grid[i][j] = "X"
                else:
                    if grid[i][j] != "■" and grid[i][j] != "X":
                        grid[i][j] = " "
    return grid


if __name__ == "__main__":
    print(pd.DataFrame(bin_tree_maze(15, 15)))
    GRID = bin_tree_maze(15, 15)
    print(pd.DataFrame(GRID))
    _, PATH = solve_maze(GRID)
    MAZE = add_path_to_grid(GRID, PATH)
    print(pd.DataFrame(MAZE))