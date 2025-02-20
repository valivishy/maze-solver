import unittest
from unittest.mock import MagicMock, patch

from cell import Cell
from maze import Maze
from window import Window


class TestMaze(unittest.TestCase):
    def setUp(self):
        """Set up a Maze instance with a mocked Window for each test."""
        self.mock_window = MagicMock(spec=Window)
        self.num_rows = 4
        self.num_cols = 4
        self.cell_size = 10
        self.maze = Maze(
            0, 0, self.num_rows, self.num_cols, self.cell_size, self.cell_size, self.mock_window, seed=42
        )

    def test_maze_initialization(self):
        """Test that the maze initializes with correct attributes."""
        self.assertEqual(self.maze._num_rows, self.num_rows)
        self.assertEqual(self.maze._num_cols, self.num_cols)
        self.assertEqual(len(self.maze._cells), self.num_rows)
        self.assertEqual(len(self.maze._cells[0]), self.num_cols)

    def test_cells_are_initialized(self):
        """Test that all cells in the maze are created and not None."""
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.assertIsInstance(self.maze._cells[row][col], Cell)

    @patch("time.sleep", return_value=None)  # To avoid delays during tests
    def test_break_entrance_and_exit(self, _):
        """Test that the entrance (top-left) and exit (bottom-right) walls are broken."""
        self.maze._break_entrance_and_exit()

        entrance_cell = self.maze._cells[0][0]
        exit_cell = self.maze._cells[-1][-1]

        self.assertFalse(entrance_cell.has_top_wall, "Top wall of entrance cell should be broken")
        self.assertFalse(exit_cell.has_bottom_wall, "Bottom wall of exit cell should be broken")

    def test_reset_cells_visited(self):
        """Test that the visited flag is reset for all cells."""
        # Simulate some cells being visited
        self.maze._cells[0][0].visited = True
        self.maze._cells[1][1].visited = True

        self.maze._reset_cells_visited()

        for row in self.maze._cells:
            for cell in row:
                self.assertFalse(cell.visited, "All cells should have visited=False after reset")

    @patch("random.randrange", return_value=0)  # To ensure deterministic wall breaking
    def test_break_walls_r(self, _):
        """Test that walls between adjacent cells are broken correctly."""
        self.maze._break_walls_r(0, 0)

        # Test specific walls after deterministic break
        current_cell = self.maze._cells[0][0]
        adjacent_cell = self.maze._cells[0][1]

        self.assertFalse(current_cell.has_right_wall, "Right wall should be broken")
        self.assertFalse(adjacent_cell.has_left_wall, "Adjacent left wall should be broken")

    @patch("time.sleep", return_value=None)
    def test_draw_cells_called(self, _):
        """Test that _draw_cell is called during cell creation."""
        with patch.object(self.maze, "_draw_cell") as mock_draw_cell:
            self.maze._create_cells()
            self.assertEqual(mock_draw_cell.call_count, self.num_rows * self.num_cols)


if __name__ == "__main__":
    unittest.main()
