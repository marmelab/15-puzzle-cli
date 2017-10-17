import sys
import os
from game.exception import GridSizeNotValidException, MoveException
from game.game import (
    build_grid, movable_tiles, move, is_grid_resolved, shuffle
)
from renderer.renderer import (
    welcome, goodbye, shuffling, victory, show_action_not_valid,
    show_grid, show_moves, show_menu_size, show_size_not_valid,
    ask_move, ask_size
)


def router(action, grid, shuffled):
    if not shuffled and action in ['s', 'S']:
        print(shuffling())
        return [shuffle(grid), True]
    else:
        return [move(grid, action), shuffled]


def play_one_turn(grid, shuffled):
    os.system('clear')
    print(show_grid(grid))
    print(show_moves(movable_tiles(grid)))

    while True:
        action = input('\n%s' % ask_move(shuffled))

        try:
            return router(action, grid, shuffled)
        except ValueError:
            print('=> ' + show_action_not_valid(action))
        except MoveException as error:
            print('=> ' + str(error))


def play(grid_arg, started_grid):
    grid, shuffled = play_one_turn(grid_arg, False)

    while not is_grid_resolved(grid, started_grid):
        grid, shuffled = play_one_turn(grid, shuffled)


def change_size():
    use_custom_size = input(show_menu_size('W')) in ['w', 'W']
    while True:
        try:
            if use_custom_size:
                size = int(input(ask_size()))
                return build_grid(size)
            return build_grid()
        except (ValueError, GridSizeNotValidException):
            print(show_size_not_valid(size))


def init():
    os.system('clear')
    print('%s\n\n' % welcome())
    grid = change_size()
    started_grid = grid.copy()
    play(grid, started_grid)
    os.system('clear')
    print(show_grid(grid))
    print('\n\n%s' % victory())


if __name__ == '__main__':
    try:
        init()
    except KeyboardInterrupt:
        print('\n' + goodbye())
        sys.exit(0)
