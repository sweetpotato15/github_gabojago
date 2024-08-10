# calculator.py
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    result = a * b 
    return result


def divide(a, b):
    result = a / b 
    return result


def pow(a, b):
    return a**b

def sqrt(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero.')
    return a**(1/b)
