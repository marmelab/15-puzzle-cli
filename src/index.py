import sys
from game.exception import MoveException
from game.game import Move, build_grid, possible_moves, move
from renderer.renderer import welcome, goodbye, show_grid, ask_move, show_moves


def init():
    print('\n\n' + welcome(), end='\n\n')
    grid = build_grid()

    while True:
        print(show_grid(grid))
        print(show_moves(possible_moves(grid)))
        direction = ask_move()
        try:
            grid = move(grid, direction)
        except MoveException as error:
            print('=> ' + str(error))


if __name__ == '__main__':
    try:
        init()
    except KeyboardInterrupt:
        print('\n' + goodbye())
        sys.exit(0)
