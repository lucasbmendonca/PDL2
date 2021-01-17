# Command.py
from Svg import Svg

def assign(command, parser):
    var = command.args['target']
    value = parser.value(command.args['source'])
    parser.vars[var] = value

def do_while(command, parser):
    value1 = int(parser.value(command.args['value1']))
    value2 = int(parser.value(command.args['value2']))
    sign = command.args['sign']
    code = command.args['code']

    inc = 1 if value2 > value1 else -1
    
    condition  = eval("value1 " + sign + " value2")

    while condition == True:
        Command.exec(code,parser)
        value1 += inc
        condition  = eval("value1 " + sign + " value2")

def do_foward(command, parser):
    value = parser.value(command.args['value'])
    print(value)
    #svg.forward

def do_right(command, parser):
    value = parser.value(command.args['value'])
    print(value)
    #svg.right

def do_left(command, parser):
    value = parser.value(command.args['value'])
    print(value)
    #svg.left

def do_back(command, parser):
    value = parser.value(command.args['value'])
    print(value)
    #svg.back

def do_setpos(command, parser):
    value = parser.value(command.args['value'])
    print(value)
    #svg.setpos

def do_setx(command, parser):
    value = parser.value(command.args['value'])
    print(value)
    #svg.setx

def do_sety(command, parser):
    value = parser.value(command.args['value'])
    print(value)
    #svg.sety

def do_home(command, parser):
    value = parser.value(command.args['value'])
    print(value)
    #svg.home

def do_pendown(command, parser):
    value = parser.value(command.args['value'])
    print(value)
    #svg.pendown

def do_penup(command, parser):
    value = parser.value(command.args['value'])
    print(value)
    #svg.penup

def do_setpencolor(command, parser):
    value = parser.value(command.args['value'])
    print(value)
    #svg.setpencolor

def do_if(command, parser):
    value1 = parser.value(command.args['value1'])
    value2 = parser.value(command.args['value2'])
    sign = command.args['sign']
    code = command.args['code']
    
    condition  = eval("value1 " + sign + " value2")

    if condition == True:
         Command.exec(code,parser)

def do_repeat(command, parser):
    value = parser.value(command.args['value'])
    print(value)
    #svg.left

class Command:
    # Dispatch Table!
    dispatch_table = {
        "assign": assign,
        "while": do_while,
        "forward": do_foward,
        "right": do_right,
        "left": do_left,
        "back": do_back,
        "setpos": do_setpos,
        "setx": do_setx,
        "sety": do_sety,
        "home": do_home,
        "pendown": do_pendown,
        "penup": do_penup,
        "setpencolor": do_setpencolor,
        "if": do_if,
        "repeat": do_repeat
    }

    def __init__(self, command, args):
        self.name = command
        self.args = args

    def __repr__(self):
        return f"Command({self.name}, {self.args})"

    def draw(self, parser):
        self.dispatch_table[self.name](self, parser)

    @classmethod
    def exec(cls, program, parser):
        for command in program:
            print(command)
            command.draw(parser)