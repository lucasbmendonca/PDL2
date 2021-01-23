# Command.py

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
    parser.svg.Forward(value)

def do_right(command, parser):
    value = parser.value(command.args['value'])
    print(value)
    parser.svg.Right(value)

def do_left(command, parser):
    value = parser.value(command.args['value'])
    parser.svg.Left(value)
    print(value)

def do_back(command, parser):
    value = parser.value(command.args['value'])
    parser.svg.Back(value)
    print(value)

def do_setpos(command, parser):
    x = parser.value(command.args['value'])
    y = parser.value(command.args['value2'])
    parser.svg.SetPos(x, y)

def do_setx(command, parser):
    x = parser.value(command.args['value'])
    print(x)
    parser.svg.SetX(x)

def do_sety(command, parser):
    y = parser.value(command.args['value'])
    parser.svg.SetY(y)
    print(y)

def do_home(command, parser):
    y = parser.value(command.args['value'])
    parser.svg.Home()

def do_pendown(command, parser):
    y = parser.value(command.args['value'])
    parser.svg.PenDown()

def do_penup(command, parser):
    y = parser.value(command.args['value'])
    parser.svg.PenUp()

def do_setpencolor(command, parser):
    value = command.args['rgb']
    arg1 = parser.value(value[0])
    arg2 = parser.value(value[1])
    arg3 = parser.value(value[2])
    parser.svg.SetPenColor(arg1, arg2, arg3)
    print(arg1, arg2,arg3)

def do_if(command, parser):
    value1 = parser.value(command.args['value1'])
    value2 = parser.value(command.args['value2'])
    sign = command.args['sign']
    code = command.args['code']
    
    condition  = eval("value1 " + sign + " value2")

    if condition == True:
         Command.exec(code,parser)
    
def do_stop(command,parser):
    Command.stop = True
    return

def do_repeat(command, parser):
    value = int(parser.value(command.args['value']))
    code = command.args['code']
    
    for _ in range(value):
        Command.exec(code,parser)
        print(value)

def do_to(command, parser):
    funcname = command.args["name"]
    code = command.args["code"]
    params = command.args["args"]
    parser.funcs[funcname] = {"code": code, "args": params}

def do_call(command, parser):
    funcname = command.args["name"]
    if funcname not in parser.funcs:
        print(f"Unknown function '{funcname}'")
        exit(1)
    params = parser.funcs[funcname]["args"]
    code = parser.funcs[funcname]["code"]
    vals = command.args["args"]

    backup_vars = parser.vars.copy()

    for var, val in zip(params, vals):
        parser.vars[var] = parser.value(val)
    Command.exec(code, parser)
    parser.vars = backup_vars.copy()

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
        "repeat": do_repeat,
        "to": do_to,
        "call": do_call,
        "stop": do_stop
    }

    stop = False

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
            if(Command.stop==True):
                Command.stop = False
                break
            command.draw(parser)