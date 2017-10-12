def start():
    return 'Welcome to the 15 puzzle game.'

SIZE = 4
MAX_SIZE = SIZE ** 2 - 1


def build_grid():
    grid = []
    for x in range(0, SIZE):
        row = []
        for y in range(0, SIZE):
            tile = x * SIZE + y + 1
            if tile > MAX_SIZE:
                tile = 0  # Corresponds to the empty box
            row.append(tile)
        grid.append(row)
    return grid
