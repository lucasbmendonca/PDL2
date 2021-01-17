import ply.yacc as yacc
from tokenizer import tokens

def p_Instruction(p):
    "instruction : command VALUE"
