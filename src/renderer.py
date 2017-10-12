from game import Move


def welcome():
    return 'Welcome to the 15 puzzle game.'


def show_grid(grid):
    grid_to_show = '\n___________________\n\n'
    for row in grid:
        for tile in row:
            if tile == 0:
                tile = '  '
            grid_to_show += '{0:<5}'.format('|' + str(tile) + '|')
        grid_to_show += '\n___________________\n\n'
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
        else:
            msg += '(L)eft '
    return msg

def ask_move():
    direction = input('Choose a direction ')
    if direction == 'T':
        return Move.TOP
    elif direction == 'R':
        return Move.RIGHT
    elif direction == 'B':
        return Move.BOTTOM
    elif direction == 'L':
        return Move.LEFT
