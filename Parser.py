# Parser.py
import sys
import ply.yacc as yacc
from Tokenizer import Lexer
from Svg import Svg
from Command import Command

class Parser:
    tokens = Lexer.tokens

    def __init__(self):
        self.parser = None
        self.lexer = None
        self.svg = Svg()
        self.vars = {}   # Symbol Table
        self.color = (0, 0, 0)

    def Parse(self, input, **kwargs):
        self.lexer = Lexer()
        self.lexer.Build(input,**kwargs)
        self.parser = yacc.yacc(module=self, **kwargs)
        program = self.parser.parse(lexer=self.lexer.lexer)
        Command.exec(program, self)

    def p_error(self, t):
        print("Syntax error", file=sys.stderr)
        exit(1)

    def p_program0(self, p):
        """  program  :   command  """
        p[0] = [p[1]]

    def p_program1(self, p):
        """  program  :  program command  """
        lst = p[1]
        lst.append(p[2])
        p[0] = lst

    def p_command0(self, p):
        """  command  :  forward value  
                      |  fd value """
        p[0] = Command("forward", {'value': p[2]})

    def p_command1(self, p):
        """  command  :  right value  
                      |  rt value """
        p[0] = Command("right", {'value': p[2]})

    def p_command2(self, p):
        """  command  :  left value  
                      |  lt value """
        p[0] = Command("left", {'value': p[2]})

    def p_command3(self, p):
        """  command  :  back value  
                      |  bk value """
        p[0] = Command("back", {'value': p[2]})
    
    def p_command4(self, p):
        """  command  :  setpos '[' value value ']' 
                        | setpos value value """
        if len(p) == 6:
            p[0] = Command("setpos", {'value1': p[3], 'value2': p[4]})
        else:
            p[0] = Command("setpos", {'value1': p[2], 'value2': p[3]})
    
    def p_command5(self, p):
        """  command  :  setx value  """
        p[0] = Command("setx", {'value': p[2]})
    
    def p_command6(self, p):
        """  command  :  sety value  """
        p[0] = Command("sety", {'value': p[2]})
    
    def p_command7(self, p):
        """  command  :  home  """
        p[0] = Command("home", {})

    def p_command8(self, p):
        """  command  :  pendown 
                      |  pd  """ 
        p[0] = Command("pendown", {})

    def p_command9(self, p):
        """  command  :  penup 
                      |  pu  """  
        p[0] = Command("penup", {})

    def p_command10(self, p):
        """  command  :  setpencolor '[' color ']'  """
        p[0] = Command("setpencolor",{
            'rgb': p[3]
        })

    def p_color(self, p):
        """  color :  value value value  """
        p[0] = (p[1], p[2], p[3])

    def p_value(self, p):
        """  value  :   NUMBER
                    |   VAR """
        p[0] = p[1]

    def p_command11(self, p):
        """  command  :   make VAR value 
                    |     make VAR expression """
        p[0] = Command("assign", {"target": p[2], "source": p[3]})

    def p_expression(self,p):
        """  expression  :   value OPERATION value """
        p[0] = Command("expression",{
            'value1': p[1],
            'op': p[2],
            'value2': p[3]
        })

    def p_command12(self, p):
        """  command  :   if value SIGN value '[' program ']'
                      |   ifelse value SIGN value '[' program ']' """

        p[0] = Command(p[1], {
            'value1': p[2],
            'sign': p[3],
            'value2': p[4],
            'code': p[6],
            })
    
    def p_command13(self, p):
        """  command  :  repeat value '[' program ']'  """
        p[0] = Command("repeat", {
            'value': p[2],
            'code': p[4]
        })
    
    def p_command14(self, p):
        """  command  :  while '[' value SIGN value ']' '[' program ']'  """
        p[0] = Command("while", {
            'min': p[5],
            'max': p[3],
            'code': p[8]
        })