import game as game


def showGrid(grid):
    for row in grid:
        for tile in row:
            print('{0:<5}'.format(tile), end='')
        print()


def startGame():
    print(game.start())

    grid = game.buildGrid()
    showGrid(grid)

startGame()
