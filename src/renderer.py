def welcome():
    return 'Welcome to the 15 puzzle game.'


def show_grid(grid):
    grid_to_show = ''
    for row in grid:
        for tile in row:
            grid_to_show += '{0:<5}'.format(tile)
        grid_to_show += '\n'
    return grid_to_show
