# Lexer.py
import ply.lex as lex
import sys

class Lexer:
    literals = "x:;,[=]()+-/*"
    t_ignore = " \n\t"
    t_DOTS = r'\.\.'
    tokens = ("INT", "STR", "NEW", "LOAD", "SAVE", "COLOR",
              "POINT", "LINE", "RECT", "RECTFILL", "POLYLINE", "CIRC",
              "FOR", "DO", "IN", "ENDFOR", "DOTS", "VAR", "RAND",
              "DEF", "ENDDEF")

    def t_COMMAND(self, t):
        r"FOR|DO|IN|END\ (DEF|FOR)|DEF|LOAD|NEW|SAVE|COLOR|POINT|RAND|LINE|RECT(FILL)?|POLYLINE|CIRC"
        t.type = t.value.replace(" ", "")
        return t

    def t_VAR(self, t):
        r"[a-wyz][0-9a-z]*"
        return t

    def t_INT(self, t):
        r"[0-9]+"
        t.value = int(t.value)
        return t

    def t_STR(self, t):
        r"""["][^"]+["]"""
        t.value = t.value[1:-1]
        return t

    def t_error(self, t):
        print(f"Parser error. Unexpected char: {t.value[0]}", file=sys.stderr)
        exit(1)

    def __init__(self):
       self.lexer = None

    def Build(self, input, **kwargs):
       self.lexer = lex.lex(module=self, **kwargs)
       self.lexer.input(input)



