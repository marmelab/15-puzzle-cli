import numpy as np
from threading import Thread, Timer
from game.random import random_move
from game.exception import SizeNotValidException, MoveException, NoEmptyTileException, NoTileFoundException


MIN_SIZE = 2
MAX_SIZE = 10
DEFAULT_SIZE = 4


def build_grid(size=DEFAULT_SIZE):
    if not MIN_SIZE <= size <= MAX_SIZE:
        raise SizeNotValidException

    grid = np.arange(size ** 2).tolist()
    grid.append(grid.pop(0))
    return np.array(grid).reshape(size, size)


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


def move(grid, tile_to_move_arg):
    tile_to_move = int(tile_to_move_arg)

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


def is_grid_resolved(grid, started_grid):
    return np.array_equal(grid, started_grid)


class ShuffleThread(Thread):
    def __init__(self, grid):
        Thread.__init__(self)
        self.grid = grid
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            self.grid = move(self.grid, random_move(movable_tiles(self.grid)))

    def stop(self):
        self.running = False

    def result(self):
        return self.grid


def shuffle(grid, timeout=1):
    shuffle_thread = ShuffleThread(grid.copy())
    time_thread = Timer(timeout, shuffle_thread.stop)

    shuffle_thread.start()
    time_thread.start()

    shuffle_thread.join()

    return shuffle_thread.result()
