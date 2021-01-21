# main.py

from Parser import Parser

with open("test0.pst", mode="r") as fh:
    contents = fh.read()

parser = Parser()
parser.Parse(contents)
