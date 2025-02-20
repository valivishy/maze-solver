import random
import time
from typing import List

from cell import Cell
from window import Window

_directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win: Window = None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells: List[List[Cell]] = [[None for _ in range(self._num_cols)] for _ in range(self._num_rows)]
        self._create_cells()
        self._seed = seed if seed is None else random.seed(seed)

    def _create_cells(self):
        for row in range(self._num_rows):
            for col in range(self._num_cols):
                x1 = self._x1 + col * self._cell_size_x
                y1 = self._y1 + row * self._cell_size_y
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y

                self._cells[row][col] = Cell(x1, y1, x2, y2, self._win)
                self._draw_cell(row, col)

    def _draw_cell(self, row, col):
        cell = self._cells[row][col]
        assert cell is not None
        cell.draw()
        self._animate()

    def _animate(self):
        if not self._win:
            return
        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1, -1)

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def _break_walls_r(self, target_row, target_column):
        visited = []

        def inner(row, column):
            print(f"visiting {row}, {column}")
            current_cell = self._cells[row][column]
            current_cell.visited = True
            visited.append((row, column))

            while True:
                to_visit = {}

                for direction in _directions:
                    temp_row, temp_column = row + direction[0], column + direction[1]
                    if min(temp_row, temp_column) < 0 or temp_row >= self._num_rows or temp_column >= self._num_cols or direction in to_visit or \
                            self._cells[temp_row][temp_column].visited or (temp_row, temp_column) in visited:
                        continue
                    to_visit[direction] = (temp_row, temp_column)
                if len(to_visit) < 1:
                    print("to_visit empty")
                    current_cell.draw()
                    break
                else:
                    direction = list(to_visit.keys())[random.randrange(0, len(to_visit))]
                    (neighbor_row, neighbor_column) = to_visit[direction]
                    print(f"directions to visit {direction}")
                    print(f"visiting next cell {neighbor_row}, {neighbor_column}")
                    new_cell = self._cells[neighbor_row][neighbor_column]
                    match direction:
                        # right
                        case (0, 1):
                            current_cell.has_right_wall = False
                            new_cell.has_left_wall = False
                        # down
                        case (1, 0):
                            current_cell.has_bottom_wall = False
                            new_cell.has_top_wall = False
                        # left
                        case (0, -1):
                            current_cell.has_left_wall = False
                            new_cell.has_right_wall = False
                        # up
                        case (-1, 0):
                            current_cell.has_top_wall = False
                            new_cell.has_bottom_wall = False
                    inner(neighbor_row, neighbor_column)

        inner(target_row, target_column)
        self._reset_cells_visited()
