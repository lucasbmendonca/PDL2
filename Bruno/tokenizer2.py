import ply.lex as lex
from utilities import slurp

class Tokenizer:
    
    tokens = (
            "FORWARD", "BACK", "LEFT", "RIGHT", 
            "SETPOS", "SETXY", "SETX", "SETY", "HOME",
            "PENDOWN", "PENUP",
            "SETPENCOLOR",
            "MAKE",
            "IF", "IFELSE",
            "REPEAT",
            "WHILE",
            "TO",
            "VALUE"
            "LEFTPAR", "RIGHTPAR",
            "LEFTSQBRACKET", "RIGHTSQBRACKET",
            )


    def __init__(self):
       self.lexer = None
       self.command = None
       self.argument = None
    

    def t_FORWARD(self, t):
        r"fd|forward"
        self.command = t.value
        print(self.command)

    def t_BACK(self, t):
        r"bk|back"
        self.command = t.value

    def t_LEFT(self, t):
        r"lt|left"
        self.command = t.value

    def t_RIGHT(self, t):
        r"rt|right"
        self.command = t.value

    def t_SETPOS(self, t):
        r"setpos"
        self.command = t.value

    def t_SETXY(self, t):
        r"setxy"
        self.command = t.value

    def t_SETX(self, t):
        r"setx"
        self.command = t.value

    def t_SETY(self, t):
        r"sety"
        self.command = t.value

    def t_HOME(self, t):
        r"home"
        self.command = t.value

    def t_VALUE(self, t):
        r"[0-9]+"
        print(t.value)
    
    def t_PENDOWN(self, t):
        r"pendown"
        self.command = t.value

    def t_PENUP(self, t):
        r"penup"
        self.command = t.value

    def t_SETPENCOLOR(self, t):
        r"setpencolor"
        self.command = t.value

    def t_MAKE(self, t):
        r"make"
        self.command = t.value
        print(self.command)

    def t_IF(self, t):
        r"if"
        self.command = t.value
    
    def t_IFELSE(self, t):
        r"ifelse"
        self.command = t.value
    
    def t_REPEAT(self, t):
        r"repeat"
        self.command = t.value
    
    def t_WHILE(self, t):
        r"while"
        self.command = t.value
    
    def t_TO(self, t):
        r"to"
        self.command = t.value


    t_ignore = "\n\s+"

    def t_error(self, t):
        t.lexer.skip(1)

    def Build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def InputFile(self, filePath):
        self.lexer.input(slurp(filePath))

    def Execute(self):
        for token in iter(self.lexer.token, None):
            print(token)

