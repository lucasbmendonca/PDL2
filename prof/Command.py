# Command.py
from Canvas import Canvas


def do_new(command, parser):
    parser.canvas = Canvas(width=parser.value(command.args['width']),
                           height=parser.value(command.args['height']),
                           color=parser.eval_color(command.args['color']))


def do_save(command, parser):
    parser.canvas.save(command.args)


def do_rect(command, parser):
    p1 = parser.eval_point(command.args['point1'])

    if 'point2' in command.args:
        p2 = parser.eval_point(command.args['point2'])
    else:
        size = parser.eval_size(command.args['size'])
        p2 = (p1[0] + size[1], p1[1] + size[2])

    color = parser.color
    if 'color' in command.args:
        color = command.args['color']

    color = parser.eval_color(color)
    parser.canvas.rect(p1, p2, color)


def do_polyline(command, parser):
    color = parser.color
    if 'color' in command.args:
        color = command.args['color']
    color = parser.eval_color(color)

    last_point = parser.eval_point(command.args['points'][0])
    for point in command.args['points'][1:]:
        pt = parser.eval_point(point)
        parser.canvas.line(last_point, pt, color)
        last_point = pt


def do_for(command, parser):
    var = command.args['var']
    min_val = parser.value(command.args['min'])
    max_val = parser.value(command.args['max'])
    code = command.args['code']

    inc = 1 if max_val > min_val else -1

    parser.vars[var] = min_val
    while parser.vars[var] <= max_val:
        Command.exec(code, parser)
        parser.vars[var] += inc

def do_assign(command, parser):
    var = command.args['target']
    value = parser.value(command.args['source'])
    parser.vars[var] = value

class Command:
    # Dispatch Table!
    dispatch_table = {
        "new": do_new,
        "save": do_save,
        "rect": do_rect,
        "polyline": do_polyline,
        "for": do_for,
        "assign": do_assign,
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
            # print(command)
            command.draw(parser)