import numpy as np
from game.Move import Move
from game.exception import MoveException, NoEmptyTileException


def build_grid(size=4):
    max_size = size ** 2 - 1
    grid = []
    for x in range(0, size):
        row = []
        for y in range(0, size):
            tile = x * size + y + 1
            if tile > max_size:
                tile = 0  # Corresponds to the empty box
            row.append(tile)
        grid.append(row)
    return np.array(grid)


def find_empty_tile(grid):
    y = 0
    while y < len(grid):
        x = 0
        while x < len(grid[y]):
            if grid[y][x] == 0:
                return [y, x]
            x += 1
        y += 1
    raise NoEmptyTileException('The grid should contain an empty tile')


def possible_moves(grid):
    y, x = find_empty_tile(grid)

    moves = []

    if not y == 0:
        moves.append(Move.TOP)
    if not x == len(grid) - 1:
        moves.append(Move.RIGHT)
    if not y == len(grid) - 1:
        moves.append(Move.BOTTOM)
    if not x == 0:
        moves.append(Move.LEFT)
    return moves


def move(grid, direction):
    y, x = find_empty_tile(grid)

    if direction not in possible_moves(grid):
        raise MoveException('This direction is not allowed')

    if direction == Move.TOP:
        new_x = x
        new_y = y - 1
    elif direction == Move.RIGHT:
        new_x = x + 1
        new_y = y
    elif direction == Move.BOTTOM:
        new_x = x
        new_y = y + 1
    elif direction == Move.LEFT:
        new_x = x - 1
        new_y = y

    new_grid = grid.copy()
    new_grid[y][x] = grid[new_y][new_x]
    new_grid[new_y][new_x] = grid[y][x]
    return new_grid
