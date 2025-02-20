from line import Line
from point import Point
from window import Window

_default_distance_from_center_to_margin = 50


class Cell:
    def __init__(self, x1: int, y1: int, x2: int, y2: int, window: Window = None):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._window = window
        self.visited = False
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    @property
    def center(self):
        return Point((self._x1 + self._x2) // 2, (self._y1 + self._y2) // 2)

    def __str__(self):
        walls = []
        if self.has_left_wall:
            walls.append("left")
        if self.has_right_wall:
            walls.append("right")
        if self.has_top_wall:
            walls.append("top")
        if self.has_bottom_wall:
            walls.append("bottom")

        return (f"Cell(center=({self.center.x}, {self.center.y}), "
                f"coordinates=(({self._x1}, {self._y1}), ({self._x2}, {self._y2})), "
                f"walls={'none' if not walls else ', '.join(walls)})")

    def draw(self):
        self._draw_line(self._x1, self._y1, self._x2, self._y1, self.has_top_wall)
        self._draw_line(self._x1, self._y2, self._x2, self._y2, self.has_bottom_wall)
        self._draw_line(self._x1, self._y1, self._x1, self._y2, self.has_left_wall)
        self._draw_line(self._x2, self._y1, self._x2, self._y2, self.has_right_wall)

    def draw_move(self, to_cell, undo=False):
        self_center = self.center
        other_center = to_cell.center
        self._window.draw_line(
            Line(
                Point(self_center.x, self_center.y),
                Point(other_center.x, other_center.y)
            ),
            "gray" if undo else "red"
        )

    def _draw_line(self, x1: int, y1: int, x2: int, y2: int, wall_exists: bool = True):
        if self._window:
            self._window.draw_line(Line(Point(x1, y1), Point(x2, y2)), 'black' if wall_exists else 'white')
