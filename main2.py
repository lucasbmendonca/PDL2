from Tokenizer import Lexer
import sys
import os

relativePath = os.path.dirname(os.path.abspath(__file__))

#Lexer
lex = Lexer()
lex.Build()
fullPath = relativePath + "\\ex5.logo"
lex.InputFile(fullPath)
lex.Execute()