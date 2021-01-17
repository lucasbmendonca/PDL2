import ply.lex as lex
from utilities import slurp
import sys

class Lexer:

    literals = """:"[]"""
    t_ignore = " \n\t"
    #t_DOTS = r'\.\.'
    tokens = (
            "forward", "fd", "back", "bk", "left", "lt", "right", 
            "rt", "setpos", "setxy", "setx", "sety", "home", "pd","pu",
            "pendown", "penup", "setpencolor", "make", "if", "ifelse", 
            "repeat", "while", "VAR", "NUMBER", "OPERATION", "SIGN")

    def t_COMMAND(self, t):
        r"(forward|fd)|(back|bk)|(left|lt)|(right|rt)|setpos|setxy|setx|sety|home|(pendown|pd)|(penup|pu)|setpencolor|make|if|ifelse|repeat|while"
        t.type = t.value.replace(" ", "")
        return t

    def t_VAR(self, t):
        r"""("|:)[a-z][0-9a-z]*"""
        return t
    
    def t_NUMBER(self, t):
        r"[-]?[0-9]+(.[0-9]+)?"
        #t.value = int(t.value)
        return t

    def t_OPERATION(self, t):
        r"[-]|[\*]|[+]|[\/]"
        return t
    
    def t_SIGN(self, t):
        r">|<|="
        return t
    
    def t_error(self, t):
        print(f"Parser error. Unexpected char: {t.value[0]}", file=sys.stderr)
        exit(1)
        #t.lexer.skip(1)

    def __init__(self):
        self.lexer = None
        self.command = None
        self.argument = None

    def Build(self, input, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        self.lexer.input(input)

    def Execute(self):
        for token in iter(self.lexer.token, None):
            print(token)

