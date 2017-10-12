def build_grid(size=4):
    max_size = size ** 2 - 1
    grid = []
    for x in range(0, size):
        row = []
        for y in range(0, size):
            tile = x * size + y + 1
            if tile > max_size:
                tile = 0  # Corresponds to the empty box
            row.append(tile)
        grid.append(row)
    return grid
