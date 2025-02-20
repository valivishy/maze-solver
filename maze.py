import time
from typing import List

from cell import Cell
from window import Window


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win: Window = None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells: List[List[Cell]] = [[None for _ in range(self._num_cols)] for _ in range(self._num_rows)]
        self._create_cells()

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
