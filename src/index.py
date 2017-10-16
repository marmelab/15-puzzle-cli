import sys
from game.exception import MoveException
from game.game import build_grid, movable_tiles, move, do_i_win, shuffle
from renderer.renderer import welcome, goodbye, shuffling, victory, show_action_not_valid, show_grid, ask_move, show_moves


def router(action, grid, shuffled):
    if not shuffled and action in ['s', 'S']:
        print(shuffling())
        return [shuffle(grid), True]
    else:
        return [move(grid, action), shuffled]


def init():
    print('\n\n%s\n\n' % welcome())
    grid = build_grid()
    started_grid = grid.copy()
    shuffled = False

    while True:
        print(show_grid(grid))
        print(show_moves(movable_tiles(grid)))
        action = input(ask_move(shuffled))

        try:
            grid, shuffled = router(action, grid, shuffled)
        except ValueError:
            print('=> ' + show_action_not_valid(action))
        except MoveException as error:
            print('=> ' + str(error))

        if do_i_win(grid, started_grid):
            print(victory())
            break

if __name__ == '__main__':
    try:
        init()
    except KeyboardInterrupt:
        print('\n' + goodbye())
        sys.exit(0)
