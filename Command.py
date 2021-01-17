# Command.py
from Svg import Svg

class Command:
    # Dispatch Table!
    def __init__(self, command, args):
        self.name = command
        self.args = args

    def __repr__(self):
        return f"Command({self.name}, {self.args})"

    #def draw(self, parser):
        #self.dispatch_table[self.name](self, parser)

    @classmethod
    def exec(cls, program, parser):
        for command in program:
            print(command)
            #command.draw(parser)