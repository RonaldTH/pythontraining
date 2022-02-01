# mathematics.py
import math

def multiply(x, y):
    return x * y

def divide(x, y):
    return round(x / y, 1)

def round_up(x):
#    rounded = int(x) + int((x > 0) and (x - int(x)) > 0)
    rounded = math.ceil(x)
    return rounded


def hypotenuse(x, y):
    return math.sqrt(x**2 + y**2)
