# main.py

from Parser import Parser

with open("c://Projeto//PDL2//prof//test0.pst", mode="r") as fh:
    contents = fh.read()

parser = Parser()
parser.Parse(contents)
