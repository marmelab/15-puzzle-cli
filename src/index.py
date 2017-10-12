from game import build_grid
from renderer import welcome, show_grid


def init():
    print(welcome())
    grid = build_grid()
    print(show_grid(grid))

if __name__ == '__main__':
    init()
