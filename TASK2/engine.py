"""
engine.py - Core arithmetic operations
"""

def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a / b

def floordiv(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a // b

def mod(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero")
    return a % b

def pow_(a, b): return a ** b

OPERATORS = {
    '+': ('Addition', add),
    '-': ('Subtraction', sub),
    '*': ('Multiplication', mul),
    '/': ('Division', div),
    '//': ('Floor division', floordiv),
    '%': ('Modulus', mod),
    '**': ('Power', pow_),
}
