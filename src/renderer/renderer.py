def welcome():
    return 'Welcome to the 15 puzzle game.'


def goodbye():
    return 'Goodbye!'


def shuffling():
    return 'Shuffling the puzzle...'


def victory():
    return 'GGWP, you solved the puzzle!'


def show_action_not_valid(action):
    return '"%s" is not a valid action' % action


def show_grid(grid):
    horizontal_line = '\n|%s|\n' % ('-' * (len(grid) * 5 - 1))
    grid_to_show = horizontal_line
    for row in grid:
        grid_to_show += '|'
        for tile in row:
            if tile == 0:
                tile = '  '
            grid_to_show += ' %s |' % '{0:>2}'.format(tile)
        grid_to_show += horizontal_line
    return grid_to_show


def show_moves(movable_tiles):
    msg = 'You are allowed to move: '

    for tile in movable_tiles:
        msg += str(tile) + ' '
    return msg


def ask_move(suffled):
    msg = 'Choose a tile to move'
    if not suffled:
        msg += ' or press (S) to shuffle'
    msg += ': '
    return msg
