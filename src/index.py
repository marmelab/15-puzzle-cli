import sys
import os
from game.exception import GridSizeNotValidException, MoveException
from game.game import (
    build_grid, movable_tiles, move, is_grid_resolved, shuffle
)
from renderer.renderer import (
    welcome, goodbye, shuffling, starting_turn,
    victory, show_action_not_valid,
    show_grid, show_moves, show_menu_size, show_size_not_valid, ask_move, ask_size
)


def router(action, grid, started_grid, shuffled):
    if not shuffled and action in ['s', 'S']:
        print(shuffling())
        return [shuffle(grid), started_grid, True]
    elif action in ['w', 'W']:
        new_grid = change_size()
        return [new_grid, new_grid.copy(), False]
    else:
        return [move(grid, action), started_grid, True]


def play_one_turn(grid, started_grid, turn_number, shuffled):
    os.system('clear')
    print(starting_turn(turn_number))
    print(show_grid(grid))
    print(show_moves(movable_tiles(grid)))

    while True:
        if not shuffled:
            action = input('\n%s' % ask_move('W', 'S'))
        else:
            action = input('\n%s' % ask_move('W', None))

        try:
            return router(action, grid, started_grid, shuffled)
        except ValueError:
            print('=> ' + show_action_not_valid(action))
        except MoveException as error:
            print('=> ' + str(error))


def play(grid_arg, started_grid_arg):
    turn_number = 1
    grid, started_grid, shuffled = play_one_turn(grid_arg, started_grid_arg, turn_number, False)
    while not shuffled or not is_grid_resolved(grid, started_grid):
        if not shuffled:
            turn_number = 1
        grid, started_grid, shuffled = play_one_turn(grid, started_grid, turn_number, shuffled)
        turn_number += 1
    return [grid, turn_number]


def change_size():
    while True:
        try:
            size = int(input(ask_size()))
            return build_grid(size)
        except (ValueError, GridSizeNotValidException):
            print(show_size_not_valid(size))


def init():
    os.system('clear')
    print('%s\n\n' % welcome())
    grid = build_grid()
    grid, turn_number = play(grid, grid.copy())
    os.system('clear')
    print('\n\n%s' % victory(turn_number))
    print(show_grid(grid))


if __name__ == '__main__':
    try:
        init()
    except KeyboardInterrupt:
        print('\n' + goodbye())
        sys.exit(0)
