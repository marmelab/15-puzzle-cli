import sys
from game import Move, build_grid, find_empty_tile, possible_moves, move
from renderer import welcome, show_grid, ask_move, show_moves
from game_exception import MoveException


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
        print('\nGoodbye')
        sys.exit(0)
