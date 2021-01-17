# PNM.py

import ply.lex as lex
import re

class PNM:

    tokens = ("P3", "PIXEL", "WIDTH", "HEIGHT")
    states = (('image', 'exclusive'), )

    def __init__(self):
        self.lexer = None
        self.width = 0
        self.height = 0
        self.image = None

        self._col = 0
        self._row = 0

    @classmethod
    def from_canvas(cls, canvas):
        self = PNM()
        self.width = canvas.width
        self.height = canvas.height
        self.image = canvas
        return self

    def load(self, filename, **kwargs):
        fh = open(filename, mode="r")
        with fh:
            contents = fh.read()
        self.lexer = lex.lex(module=self, **kwargs)
        self.lexer.input(contents)
        self.lexer.token()

    def save(self, filename):
        fh = open(filename, mode="w+")
        with fh:
            print("P3", file=fh)
            print(f"{self.width} {self.height}\n255", file=fh)
            for y in range(0, self.height):
                for x in range(0, self.width):
                    print("%d %d %d" % self.image[(x, y)][:], file=fh, end=" ")
                print("", file=fh)

    def t_image_error(self, t):
        self.t_error(t)

    def t_error(self, t):
        print(f"Unexpected token: '{t.value[0]}'")
        exit(1)

    def t_P3(self, t):
        r"P3\n"
        pass

    def t_WIDTH(self, t):
        r"[0-9]+[ ]"
        self.width = int(t.value)
        pass

    def t_HEIGHT(self, t):
        r"[0-9]+\n"
        if self.height == 0:
            from Canvas import Canvas
            self.height = int(t.value)
            self.image = Canvas(self.width, self.height)
        else:
            t.lexer.begin('image')
        pass

    def t_image_PIXEL(self, t):
        r"([0-9]+[ \t\n]*){3}"   # '0 0 0 ' => "0" "0" "0" ""
        lst = re.split(r"[ \t\n]+", t.value)
        (r, g, b) = [int(n) for n in lst[:3]]  # linq.select / map
        self.image[(self._col, self._row)] = (r, g, b)
        self._col += 1
        if self._col >= self.width:
            self._row += 1
            self._col = 0
        pass


