from line import Line
from point import Point
from window import Window
_default_distance_from_center_to_margin = 50


class Cell:
    def __init__(self, center: Point, window: Window):
        self._x1 = center.x - _default_distance_from_center_to_margin
        self._y1 = center.y - _default_distance_from_center_to_margin
        self._x2 = center.x + _default_distance_from_center_to_margin
        self._y2 = center.y + _default_distance_from_center_to_margin
        self.center = center
        self._window = window
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

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
        if self.has_top_wall:  # Horizontal top wall
            self._draw_line(self._x1, self._y1, self._x2, self._y1)
        if self.has_bottom_wall:  # Horizontal bottom wall
            self._draw_line(self._x1, self._y2, self._x2, self._y2)
        if self.has_left_wall:  # Vertical left wall
            self._draw_line(self._x1, self._y1, self._x1, self._y2)
        if self.has_right_wall:  # Vertical right wall
            self._draw_line(self._x2, self._y1, self._x2, self._y2)

    def draw_move(self, to_cell, undo=False):
        print(self)
        print(to_cell)
        self_center = self.center
        other_center = to_cell.center
        self._window.draw_line(
            Line(
                Point(self_center.x, self_center.y),
                Point(other_center.x, other_center.y)
            ),
            "gray" if undo else "red"
        )

    def _draw_line(self, x1: int, y1: int, x2: int, y2: int):
        self._window.draw_line(Line(Point(x1, y1), Point(x2, y2)), "black")
