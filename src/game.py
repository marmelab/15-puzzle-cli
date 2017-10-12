from enum import Enum


class Move(Enum):
    TOP = 1
    RIGHT = 2
    BOTTOM = 3
    LEFT = 4


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
    return grid



def find_empty_tile(grid):
    y = 0
    while y < len(grid):
        x = 0
        while x < len(grid[y]):        
            if grid[y][x] == 0:
                return [y, x]
            x+=1
        y+=1
    return [-1, -1]


def possible_moves(grid):
    empty_tile = find_empty_tile(grid)
    moves = []

    if empty_tile == [-1, -1]:
        return moves;

    if empty_tile[0] != 0:
        moves.append(Move.TOP)
    if empty_tile[1] != len(grid) - 1:
        moves.append(Move.RIGHT)
    if empty_tile[0] != len(grid) - 1:
        moves.append(Move.BOTTOM)
    if empty_tile[1] != 0:
        moves.append(Move.LEFT)
    return moves


def move(grid, direction):
    empty_tile = find_empty_tile(grid)

    if direction not in possible_moves(grid) or empty_tile == [-1, -1]:
        return grid

    if direction == Move.TOP:
        new_empty_tile = [empty_tile[0] - 1, empty_tile[1]]
    elif direction == Move.RIGHT:
        new_empty_tile = [empty_tile[0], empty_tile[1] + 1]
    elif direction == Move.BOTTOM:
        new_empty_tile = [empty_tile[0] + 1, empty_tile[1]]
    elif direction == Move.LEFT:
        new_empty_tile = [empty_tile[0], empty_tile[1] - 1]
    else:
        raise Exception('The direction provided to the move function is not allowed')

    value = grid[empty_tile[0]][empty_tile[1]]
    grid[empty_tile[0]][empty_tile[1]] = grid[new_empty_tile[0]][new_empty_tile[1]] 
    grid[new_empty_tile[0]][new_empty_tile[1]] = value

    return grid
