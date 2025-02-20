from window import Window
from maze import Maze


def main():
    window = Window(800, 600)
    maze = Maze(0, 0, 30, 30, 50, 50, window, 4)

    if maze.solve():
        print("Solution found !")
    else:
        print("No solution found !")

    window.wait_for_close()


if __name__ == '__main__':
    main()
