from enum import Enum
import math
import list
import string

__all__ = ["calculations", "ceil", "Method"]

Method = Enum('Method', ["add", "subtract", "multiply", "divide"])


def calculations(method_name: Method, first: int, second: int):
    match method_name:
        case Method.add.value:
            return first + second
        case Method.subtract.value:
            return first - second
        case Method.multiply.value:
            return first * second
        case Method.divide.value:
            return first / second


def ceil(decimal: float):
    return math.ceil(decimal)


def math_functions():  # pragma: no cover
    add_result = calculations(Method.add.value, 1, 2)
    subtract_result = calculations(Method.subtract.value, 50, 30)
    multiply_result = calculations(Method.multiply.value, 50, 30)
    divide_result = calculations(Method.divide.value, 50, 10)
    ceil_result = ceil(3.11)

    print("Add Result = ", add_result)
    print("Subtract Result = ", subtract_result)
    print("Multiply Result = ", multiply_result)
    print("Divide Result = ", divide_result)
    print("Ceil Result = ", ceil_result)


if __name__ == "__main__": # pragma: no cover
    print('--------****MATH****--------')
    math_functions()
    print('--------****LIST****--------')
    list.list_functions()
    print('--------****STRING****--------')
    string.string_functions()
