# main.py
from Parser import Parser
import sys
import os

relativePath = os.path.dirname(os.path.abspath(__file__))
fullPath = relativePath + "\\ex10.logo"

with open(fullPath, mode="r") as fh:
    contents = fh.read()

parser = Parser()
parser.Parse(contents)
parser.svg.SaveSVG()
parser.svg.display()