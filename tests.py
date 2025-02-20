import unittest
from maze import Maze
import unittest
from unittest.mock import MagicMock
from cell import Cell
from point import Point
from line import Line
from window import Window


class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 10
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )


class TestCell(unittest.TestCase):
    def setUp(self):
        """Initialize a Cell instance with a mocked Window before each test."""
        self.mock_window = MagicMock(spec=Window)
        self.cell = Cell(0, 0, 10, 10, self.mock_window)

    def test_initial_attributes(self):
        """Test that the Cell initializes with the correct coordinates and walls."""
        self.assertEqual(self.cell._x1, 0)
        self.assertEqual(self.cell._y1, 0)
        self.assertEqual(self.cell._x2, 10)
        self.assertEqual(self.cell._y2, 10)

        self.assertTrue(self.cell.has_left_wall)
        self.assertTrue(self.cell.has_right_wall)
        self.assertTrue(self.cell.has_top_wall)
        self.assertTrue(self.cell.has_bottom_wall)

    def test_center_property(self):
        """Test that the center property returns the correct Point."""
        expected_center = Point(5, 5)
        self.assertEqual(self.cell.center.x, expected_center.x)
        self.assertEqual(self.cell.center.y, expected_center.y)

    def test_str_representation_with_all_walls(self):
        """Test string representation when all walls are present."""
        expected_str = (
            "Cell(center=(5, 5), coordinates=((0, 0), (10, 10)), walls=left, right, top, bottom)"
        )
        self.assertEqual(str(self.cell), expected_str)

    def test_str_representation_with_no_walls(self):
        """Test string representation when no walls are present."""
        self.cell.has_left_wall = False
        self.cell.has_right_wall = False
        self.cell.has_top_wall = False
        self.cell.has_bottom_wall = False

        expected_str = "Cell(center=(5, 5), coordinates=((0, 0), (10, 10)), walls=none)"
        self.assertEqual(str(self.cell), expected_str)

    def test_draw_calls_window_draw_line(self):
        """Test that draw calls the window's draw_line method the correct number of times."""
        self.cell.draw()
        self.assertEqual(self.mock_window.draw_line.call_count, 4)  # One for each wall

    def test_draw_move_calls_window_draw_line(self):
        """Test that draw_move calls window.draw_line with correct parameters."""
        target_cell = Cell(10, 0, 20, 10, self.mock_window)
        self.cell.draw_move(target_cell)

        self.mock_window.draw_line.assert_called_with(
            Line(Point(5, 5), Point(15, 5)), "red"
        )

    def test_draw_move_undo_calls_window_draw_line_with_gray(self):
        """Test that draw_move with undo=True uses gray color."""
        target_cell = Cell(10, 0, 20, 10, self.mock_window)
        self.cell.draw_move(target_cell, undo=True)

        self.mock_window.draw_line.assert_called_with(
            Line(Point(5, 5), Point(15, 5)), "gray"
        )


if __name__ == "__main__":
    unittest.main()
