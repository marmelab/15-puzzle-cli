from game.Move import Move


def welcome():
    return 'Welcome to the 15 puzzle game.'


def goodbye():
    return 'Goodbye!'


def show_grid(grid):
    horizontal_line = '\n|' + ('-' * (len(grid) * 5 - 1)) + '|\n'
    grid_to_show = horizontal_line
    for row in grid:
        grid_to_show += '|'
        for tile in row:
            if tile == 0:
                tile = '  '
            grid_to_show += ' ' + '{0:>2}'.format(tile) + ' |'
        grid_to_show += horizontal_line
    return grid_to_show


def show_moves(possible_moves):
    msg = 'You are allowed to go: '

    for move in possible_moves:
        if move == Move.TOP:
            msg += '(T)op '
        elif move == Move.RIGHT:
            msg += '(R)ight '
        elif move == Move.BOTTOM:
            msg += '(B)ottom '
        elif move == Move.LEFT:
            msg += '(L)eft '
    return msg


def ask_move():
    direction = input('Choose a direction: ')
    if direction in ['T', 't']:
        return Move.TOP
    elif direction in ['R', 'r']:
        return Move.RIGHT
    elif direction in ['B', 'b']:
        return Move.BOTTOM
    elif direction in ['L', 'l']:
        return Move.LEFT
