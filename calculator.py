# calculator.py
def add(a, b):
    return a+b

def subtract(a, b):
    pass

def multiply(a, b):
    pass

def divide(a, b):
    pass

def pow(a, b):
    return a**b

def sqrt(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero.')
    return a**(1/b)