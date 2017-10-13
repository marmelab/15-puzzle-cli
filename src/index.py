from game import Move, build_grid, find_empty_tile, possible_moves, move
from renderer import welcome, show_grid, ask_move, show_moves
from game_exception import MoveException


def init():
    print('\n\n' + welcome(), end='\n\n')
    grid = build_grid()

    while True:
        print(show_grid(grid))
        print(show_moves(possible_moves(grid)))
        try:
            direction = ask_move()
            grid = move(grid, direction)
        except MoveException as error:
            print(error)


if __name__ == '__main__':
    init()
