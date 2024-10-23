import ply.yacc as yacc
import math
from lexer import tokens

# Precedence rules to handle operator precedence and associativity
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'POWER'),
    ('left', 'SIN', 'COS', 'TAN', 'LOG', 'EXP')
)

# Grammar rules
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression POWER expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        if p[3] == 0:
            raise ZeroDivisionError("Division by zero")
        p[0] = p[1] / p[3]
    elif p[2] == '^':
        p[0] = math.pow(p[1], p[3])

def p_expression_uminus(p):
    'expression : MINUS expression %prec MINUS'
    p[0] = -p[2]

def p_expression_group(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

def p_expression_sin(p):
    'expression : SIN LPAREN expression RPAREN'
    p[0] = math.sin(p[3])

def p_expression_cos(p):
    'expression : COS LPAREN expression RPAREN'
    p[0] = math.cos(p[3])

def p_expression_tan(p):
    'expression : TAN LPAREN expression RPAREN'
    p[0] = math.tan(p[3])

def p_expression_log(p):
    'expression : LOG LPAREN expression RPAREN'
    if p[3] <= 0:
        raise ValueError("Logarithm of non-positive number")
    p[0] = math.log(p[3])

def p_expression_exp(p):
    'expression : EXP LPAREN expression RPAREN'
    p[0] = math.exp(p[3])

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

