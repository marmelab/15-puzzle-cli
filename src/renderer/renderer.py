import numpy as np


def welcome():
    return 'Welcome to the 15 puzzle game.'


def goodbye():
    return 'Goodbye!'


def shuffling():
    return 'Shuffling the puzzle...'


def starting_turn(turn_number):
    return 'Turn %s' % turn_number


def victory(turn_number):
    return 'GGWP, you solved the puzzle in %s turns!' % (turn_number - 1)


def show_action_not_valid(action):
    return '"%s" is not a valid action' % action


def build_line(start_symb, stop_symb, sep_symb, line):
    return '\n%s%s%s\n' % (start_symb, sep_symb.join(line), stop_symb)


def show_grid(grid):
    size = len(grid)

    tile_line = np.full(size, '─' * 4).tolist()

    horizontal_line = build_line('├', '┤', '┼', tile_line)
    first_horizontal_line = build_line('┌', '┐', '┬', tile_line)
    last_horizontal_line = build_line('└', '┘', '┴', tile_line)

    grid_to_show = first_horizontal_line
    for count, row in enumerate(grid):
        grid_to_show += '│'
        for tile in row:
            if tile == 0:
                tile = '  '
            grid_to_show += ' %s │' % '{0:>2}'.format(tile)
        if not count == size - 1:
            grid_to_show += horizontal_line
    grid_to_show += last_horizontal_line
    return grid_to_show


def show_moves(movable_tiles):
    return 'You are allowed to move (%s)' % ', '.join(map(str, movable_tiles))


def show_menu_size(key):
    return 'Press (%s) to change the puzzle size, press any other key to use the default one: ' % key


def show_size_not_valid(size):
    return 'Sorry, "%s" is not a valid size' % size


def ask_move(key_resize, key_shuffle):
    msg = 'Choose a tile to move'
    if key_resize:
        msg += ' or press (%s) to resize' % key_resize
    if key_shuffle:
        msg += ' or press (%s) to shuffle' % key_shuffle
    msg += ': '
    return msg


def ask_size(min_size=2, max_size=10):
    return 'Choose a new size (from %s to %s): ' % (min_size, max_size)
