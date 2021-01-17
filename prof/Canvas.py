# Canvas.py

from PNM import PNM
import math


def _build_canvas(w, h, color=(0, 0, 0)):
    return [[color for _ in range(0, h)] for _ in range(0, w)]


def _min_max(a, b):
    return (a, b) if a < b else (b, a)


class Canvas:

    def __init__(self, width, height, color=(0, 0, 0)):
        self.width = width
        self.height = height
        if type(color) == tuple and len(color) == 3:
            self.canvas = _build_canvas(width, height, color=color)
        else:
            raise Exception("Color must be a triple")

    @classmethod
    def from_file(cls, filename, **kwargs):
        pnm = PNM()
        pnm.load(filename, **kwargs)
        return pnm.image

    def save(self, filename):
        pnm = PNM.from_canvas(self)
        pnm.save(filename)

    def point(self, point, color):
        if self._valid_point(point):
            self[point] = color

    def _valid_point(self, point):
        x, y = point
        if x < 0 or y < 0 or x >= self.width or y >= self.height:
            raise Exception("Point with index out of canvas size")
        return True

    def rect(self, point_a, point_b, color):
        if self._valid_point(point_a) and self._valid_point(point_b):
            x0, y0 = point_a
            x1, y1 = point_b
            self.line((x0, y0), (x1, y0), color)
            self.line((x1, y0), (x1, y1), color)
            self.line((x1, y1), (x0, y1), color)
            self.line((x0, y1), (x0, y0), color)

    def rectfill(self, point_a, point_b, color):
        if self._valid_point(point_a) and self._valid_point(point_b):
            y_min, y_max = _min_max(point_a[1], point_b[1])
            x_min, x_max = _min_max(point_a[0], point_b[0])
            for x in range(x_min, x_max+1):
                for y in range(y_min, y_max+1):
                    self[(x, y)] = color

    def circ(self, center, radius, color):
        if self._valid_point(center):
            theta = 0
            while theta <= 2 * math.pi:
                x = math.sin(theta) * radius + center[0]
                y = math.cos(theta) * radius + center[1]
                if self._valid_point((x, y)):
                    self[(x, y)] = color
                theta += math.pi / (2 * radius)

    def line(self, point_a, point_b, color):
        if self._valid_point(point_a) and self._valid_point(point_b):
            y_min, y_max = _min_max(point_a[1], point_b[1])
            x_min, x_max = _min_max(point_a[0], point_b[0])

            horizontal = abs(point_a[0] - point_b[0]) > abs(point_a[1] - point_b[1])

            if horizontal:
                # y0 = m * x0 + b
                # y1 = m * x1 + b
                #
                # b = y0 - m * x0
                # y1 = m * x1 + y0 - m * x0
                # y1 = m * (x1 - x0) + y0
                # m = (y1-y0)/(x1-x0)
                m = (point_b[1] - point_a[1]) / (point_b[0] - point_a[0])
                b = point_a[1] - m * point_a[0]

                for x in range(x_min, x_max + 1):
                    y = m * x + b
                    self[(x, y)] = color
            else:
                m = (point_b[0] - point_a[0]) / (point_b[1] - point_a[1])
                b = point_a[0] - m * point_a[1]

                for y in range(y_min, y_max + 1):
                    x = m * y + b
                    self[(x, y)] = color

    def __getitem__(self, item):
        if type(item) == tuple and len(item) == 2:
            x, y = item
            return self.canvas[int(x)][int(y)]
        else:
            raise IndexError("Canvas index should be a tuple pair")

    def __setitem__(self, key, value):
        if type(key) == tuple and len(key) == 2:
            if type(value) == tuple and len(value) == 3:
                x, y = key
                self.canvas[int(x)][int(y)] = value
            else:
                raise Exception("Color should be a tuple of size 3.")
        else:
            raise IndexError("Canvas index should be a tuple pair")

