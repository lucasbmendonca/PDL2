# Parser.py
import sys
import random
import ply.yacc as yacc
from Lexer import Lexer
from Canvas import Canvas
from Command import Command


class Parser:
    tokens = Lexer.tokens

    def __init__(self):
        self.parser = None
        self.lexer = None
        self.canvas = None
        self.vars = {}   # Symbol Table
        self.color = (0, 0, 0)

    def eval_point(self, point):
        return (self.value(point[0]), self.value(point[1]))

    def eval_size(self, size):
        return (size[0], self.value(size[1]), self.value(size[2]))

    def eval_color(self, color):
        return (self.value(color[0]), self.value(color[1]), self.value(color[2]))

    def value(self, val):
        if type(val) == dict:
            max_val = val['rand']
            max_val = self.value(max_val)
            return random.randint(1, max_val)   ## should be zero in the future FIXME

        if type(val) == int:
            return val

        if val in self.vars:
            return self.vars[val]

        print(f"Variable {val} undefined")
        self.vars[val] = 0
        return 0

    def Parse(self, input, **kwargs):
        self.lexer = Lexer()
        self.lexer.Build(input, **kwargs)
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
        """  command  :  NEW size color ';'  """
        p[0] = Command("new", {'width': p[2][1], 'height': p[2][2], 'color': p[3]})

    def p_command1(self, t):
        """  command  :  LOAD STR ';'  """

    def p_command2(self, p):
        """  command  :  SAVE STR ';'  """
        p[0] = Command("save", p[2])

    def p_command3(self, t):
        """  command  :  COLOR color ';'  """

    def p_command4(self, t):
        """  command  :  POINT point color ';'
                      | POINT point ';' """
        # ....

    def p_command5(self, t):
        """  command  :  LINE  point point color ';'
                      | LINE point point ';'  """

    def p_command6(self, p):
        """  command  :  RECT  point point color ';'
                      |  RECT  point size color ';'
                      |  RECT  point point ';'
                      |  RECT  point size ';'      """
        args = {'point1': p[2]}

        if len(p) == 6:
            args['color'] = p[4]

        if len(p[3]) == 3:
            args['size'] = p[3]
        else:
            args['point2'] = p[3]

        p[0] = Command("rect", args)

    def p_command7(self, t):
        """  command  :  RECTFILL  point point color ';'
                      |  RECTFILL  point size color ';'
                      |  RECTFILL  point point ';'
                      |  RECTFILL  point size ';'      """

    def p_command8(self, t):
        """  command  :  CIRC  point INT color ';'
                      | CIRC point INT ';'  """

    def p_command9(self, p):
        """  command  :  POLYLINE points color ';'
                      |  POLYLINE points ';'  """
        args = {"points": p[2]}
        if len(p) == 5:
            args['color'] = p[3]
        p[0] = Command("polyline", args)

    def p_command_for(self, p):
        """  command  :  FOR VAR IN '[' value DOTS value ']' DO program ENDFOR ';' """
        p[0] = Command("for", {
            'var': p[2],
            'min': p[5],
            'max': p[7],
            'code': p[10]
        })

    def p_command_10(self, p):
        """   command  :   VAR '=' value ';' """
        p[0] = Command("assign", {"target": p[1], "source": p[3]})


    def p_points0(self, p):
        """  points  :  point  """
        p[0] = [p[1]]

    def p_points1(self, p):
        """  points  :  points point  """
        p[1].append(p[2])
        p[0] = p[1]

    def p_point(self, p):
        """  point : value ',' value """
        p[0] = (p[1], p[3])

    def p_size(self, p):
        """  size : value 'x' value """
        p[0] = ("size", p[1], p[3])

    def p_color(self, p):
        """  color :  value ':' value ':' value  """
        p[0] = (p[1], p[3], p[5])

    def p_value(self, p):
        """  value  :   INT
                    |   VAR
                    |   RAND value """
        if len(p) == 2:
            p[0] = p[1]
        else:
            p[0] = {'rand': p[2]}
