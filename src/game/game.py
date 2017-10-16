import numpy as np
from game.exception import MoveException, NoEmptyTileException, NoTileFoundException


def build_grid(size=4):
    grid = np.arange(size ** 2).tolist()
    grid.append(grid.pop(0))
    return np.array(grid).reshape(4, 4)


def find_tile(grid, value):
    y = 0
    while y < len(grid):
        x = 0
        while x < len(grid[y]):
            if int(grid[y][x]) == int(value):
                return [y, x]
            x += 1
        y += 1
    raise NoTileFoundException('The grid does not contain this tile')


def find_empty_tile(grid):
    try:
        return find_tile(grid, 0)
    except NoTileFoundException:
        raise NoEmptyTileException


def movable_tiles(grid):
    length = len(grid)
    y, x = find_empty_tile(grid)

    tiles = []
    if y - 1 >= 0:
        tiles.append(grid[y - 1][x])
    if x + 1 < length:
        tiles.append(grid[y][x + 1])
    if y + 1 < length:
        tiles.append(grid[y + 1][x])
    if x - 1 >= 0:
        tiles.append(grid[y][x - 1])

    return list(map(int, tiles))


def move(grid, tile_to_move):
    try:
        tile_to_move = int(tile_to_move)
    except ValueError:
        raise MoveException('The tile to move should be an integer')

    if tile_to_move not in movable_tiles(grid):
        raise MoveException('This tile cannot be moved')

    try:
        empty_y, empty_x = find_empty_tile(grid)
        new_y, new_x = find_tile(grid, tile_to_move)
    except NoEmptyTileException:
        raise MoveException('There is not empty tile to move this tile')
    except NoTileFoundException:
        raise MoveException('This tile does not exist')

    new_grid = grid.copy()
    new_grid[empty_y][empty_x] = grid[new_y][new_x]
    new_grid[new_y][new_x] = grid[empty_y][empty_x]
    return new_grid
