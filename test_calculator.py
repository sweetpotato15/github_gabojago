# test_calculator.py
# import pytest
from calculator import add, subtract, multiply, divide, pow, sqrt

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(-1, -1) == 0

def test_multiply():
    assert multiply (2, 3) == 6

def test_divide():
    assert divide (2, 3) == 1.5

def test_pow():
    assert pow(2,3) == 8
    assert pow(3,4) == 81

def test_sqrt():
    assert sqrt(16,2) == 4
    assert sqrt(36,2) == 6
