# Command.py
from Svg import Svg

def assign(command, parser):
    var = command.args['target']
    value = parser.value(command.args['source'])
    parser.vars[var] = value

def do_while(command, parser):
    var = command.args['target']
    value = parser.value(command.args['source'])
    parser.vars[var] = value

def do_foward(command, parser):
    var = command.args['target']
    value = parser.value(command.args['source'])
    parser.vars[var] = value

def do_right(command, parser):
    var = command.args['target']
    value = parser.value(command.args['source'])
    parser.vars[var] = value

class Command:
    # Dispatch Table!
    dispatch_table = {
        "assign": assign,
        "while": do_while,
        "foward": do_foward,
        "right": do_right
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