import sys
from game.exception import MoveException
from game.game import build_grid, movable_tiles, move, shuffle
from renderer.renderer import welcome, goodbye, show_action_not_valid, show_grid, ask_move, show_moves


def router(action, grid, shuffled):
    if not shuffled and action in ['s', 'S']:
        return [shuffle(grid), True]
    else:
        return [move(grid, action), shuffled]


def init():
    print('\n\n' + welcome(), end='\n\n')
    grid = build_grid()
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


if __name__ == '__main__':
    try:
        init()
    except KeyboardInterrupt:
        print('\n' + goodbye())
        sys.exit(0)
