import game


def show_grid(grid):
    for row in grid:
        for tile in row:
            print('{0:<5}'.format(tile), end='')
        print()


def start_game():
    print(game.start())

    grid = game.build_grid()
    show_grid(grid)

start_game()
