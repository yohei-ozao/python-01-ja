def add(a, b):
    if type(a) is int and type(b) is int:
        result = int(a) + int(b)
        return result
    else:
        return "bad input"


def subtract(a, b):
    if type(a) is int and type(b) is int:
        result = int(a) - int(b)
        return result
    else:
        return "bad input"


def multiply(a, b):
    if type(a) is int and type(b) is int:
        result = int(a) * int(b)
        return result
    else:
        return "bad input"


def divide(a, b):
    import numpy as np
    if type(a) is int and type(b) is int:
        try: 
            return int(a) / int(b) 
        except ZeroDivisionError:
            return "Cannot divide by zero"
    else:
        return "bad input"

# a = input("a: ")
# b = input("b: ")
# print(add(a,b))
#print(add("5", 5))