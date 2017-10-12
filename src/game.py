# Start the game


def start():
    return 'Welcome to the 15 puzzle game.'

# Grid management


def buildGrid():
    grid = []
    for x in range(0, 4):
        row = []
        for y in range(0, 4):
            tile = x * 4 + y + 1
            if tile > 15:
                tile = 0  # Corresponds to the empty box
            row.append(tile)
        grid.append(row)
    return grid
