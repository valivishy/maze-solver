from tkinter import Canvas

from point import Point


class Line:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def __eq__(self, other):
        return isinstance(other, Line) and self.start == other.start and self.end == other.end

    def __hash__(self):
        return hash((self.start, self.end))

    def draw(self, canvas: Canvas, fill_color: str):
        canvas.create_line(
            self.start.x, self.start.y, self.end.x, self.end.y, fill=fill_color, width=2
        )
