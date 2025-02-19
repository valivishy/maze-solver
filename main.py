from cell import Cell
from window import Window
from point import Point


def main():
    window = Window(800, 600)

    # Scenario 1: Fully walled cell (all walls present)
    cell_fully_walled = Cell(Point(30, 30), window)
    cell_fully_walled.draw()

    # Scenario 2: Cell with only the left wall
    cell_left_wall_only = Cell(Point(80, 30), window)
    cell_left_wall_only.has_right_wall = False
    cell_left_wall_only.has_top_wall = False
    cell_left_wall_only.has_bottom_wall = False
    cell_left_wall_only.draw()

    # Scenario 3: Cell with only the right wall
    cell_right_wall_only = Cell(Point(130, 30), window)
    cell_right_wall_only.has_left_wall = False
    cell_right_wall_only.has_top_wall = False
    cell_right_wall_only.has_bottom_wall = False
    cell_right_wall_only.draw()

    # Scenario 4: Cell with only the top wall
    cell_top_wall_only = Cell(Point(180, 30), window)
    cell_top_wall_only.has_left_wall = False
    cell_top_wall_only.has_right_wall = False
    cell_top_wall_only.has_bottom_wall = False
    cell_top_wall_only.draw()

    # Scenario 5: Cell with only the bottom wall
    cell_bottom_wall_only = Cell(Point(230, 30), window)
    cell_bottom_wall_only.has_left_wall = False
    cell_bottom_wall_only.has_right_wall = False
    cell_bottom_wall_only.has_top_wall = False
    cell_bottom_wall_only.draw()

    # Scenario 6: Cell with left and right walls only
    cell_left_right_walls = Cell(Point(30, 80), window)
    cell_left_right_walls.has_top_wall = False
    cell_left_right_walls.has_bottom_wall = False
    cell_left_right_walls.draw()

    # Scenario 7: Cell with top and bottom walls only
    cell_top_bottom_walls = Cell(Point(80, 80), window)
    cell_top_bottom_walls.has_left_wall = False
    cell_top_bottom_walls.has_right_wall = False
    cell_top_bottom_walls.draw()

    # Scenario 8: Cell with no walls
    cell_no_walls = Cell(Point(130, 80), window)
    cell_no_walls.has_left_wall = False
    cell_no_walls.has_right_wall = False
    cell_no_walls.has_top_wall = False
    cell_no_walls.has_bottom_wall = False
    cell_no_walls.draw()

    # Scenario 9: Cell with left and top walls
    cell_left_top_walls = Cell(Point(180, 80), window)
    cell_left_top_walls.has_right_wall = False
    cell_left_top_walls.has_bottom_wall = False
    cell_left_top_walls.draw()

    # Scenario 10: Cell with right and bottom walls
    cell_right_bottom_walls = Cell(Point(230, 80), window)
    cell_right_bottom_walls.has_left_wall = False
    cell_right_bottom_walls.has_top_wall = False
    cell_right_bottom_walls.draw()
    cell_left_wall_only.draw_move(cell_right_bottom_walls)

    window.wait_for_close()


if __name__ == '__main__':
    main()
