from graphics import Point, Line

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.window = win
        self.visited = False

    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        if self.has_left_wall:
            self.window.draw_line(Line(Point(x1, y1), Point(x1, y2)))
        else:
            self.window.draw_line(Line(Point(x1, y1), Point(x1, y2)), "white")
        if self.has_top_wall:
            self.window.draw_line(Line(Point(x1, y1), Point(x2, y1)))
        else:
            self.window.draw_line(Line(Point(x1, y1), Point(x2, y1)), "white")
        if self.has_right_wall:
            self.window.draw_line(Line(Point(x2, y1), Point(x2, y2)))
        else:
            self.window.draw_line(Line(Point(x2, y1), Point(x2, y2)), "white")
        if self.has_bottom_wall:
            self.window.draw_line(Line(Point(x1, y2), Point(x2, y2)))
        else:
            self.window.draw_line(Line(Point(x1, y2), Point(x2, y2)), "white")

    def draw_move(self, to_cell, undo=False):
        half_length = (self.x2 - self.x1) / 2
        x_center = self.x1 + half_length
        y_center = self.y1 + half_length

        half_length2 = (to_cell.x2 - to_cell.x1) / 2
        x_center2 = to_cell.x1 + half_length2
        y_center2 = to_cell.y1 + half_length2

        fill_color = "red"
        if undo:
            fill_color = "grey"

        line = Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self.window.draw_line(line, fill_color)