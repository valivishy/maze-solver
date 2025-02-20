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
        self._seed = seed if seed is None else random.seed(seed ** 15)
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)

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
        time.sleep(0.01)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[-1][-1].has_bottom_wall = False
        self._draw_cell(-1, -1)
        self._animate()

    def _reset_cells_visited(self):
        for row in self._cells:
            for cell in row:
                cell.visited = False

    def _break_walls_r(self, target_row, target_column):
        visited = []

        def inner(row, column):
            self._animate()
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
                    current_cell.draw()
                    break
                else:
                    direction = list(to_visit.keys())[random.randrange(0, len(to_visit))]
                    (neighbor_row, neighbor_column) = to_visit[direction]
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

    def solve(self) -> bool:
        return self.solve_r(0, 0)

    @staticmethod
    def can_move(direction, current_cell, next_cell):
        wall_mapping = {
            (0, 1): ("has_right_wall", "has_left_wall"),   # Right
            (1, 0): ("has_bottom_wall", "has_top_wall"),   # Down
            (0, -1): ("has_left_wall", "has_right_wall"),  # Left
            (-1, 0): ("has_top_wall", "has_bottom_wall"),  # Up
        }

        current_wall, next_wall = wall_mapping.get(direction, (None, None))

        if current_wall and getattr(current_cell, current_wall):
            print(f"Blocked: current cell has {current_wall.replace('_', ' ')}.")
            return False

        if next_wall and getattr(next_cell, next_wall):
            print(f"Blocked: next cell has {next_wall.replace('_', ' ')}.")
            return False

        print("Move allowed.")
        return True

    def solve_r(self, row, column) -> bool:
        self._animate()
        current_cell = self._cells[row][column]
        current_cell.visited = True

        if row == self._num_rows - 1 and column == self._num_cols - 1:
            return True

        for direction in _directions:
            next_cell_row, next_cell_column = row + direction[0], column + direction[1]
            if min(next_cell_row, next_cell_column) < 0 or next_cell_row >= self._num_rows or next_cell_column >= self._num_cols:
                continue

            next_cell = self._cells[next_cell_row][next_cell_column]
            if next_cell.visited:
                continue

            if self.can_move(direction, current_cell, next_cell):
                current_cell.draw_move(next_cell)
                self._animate()
                if self.solve_r(next_cell_row, next_cell_column):
                    return True
                else:
                    current_cell.draw_move(next_cell, True)
                    self._animate()
        return False

