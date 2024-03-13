import math
from enum import Enum

__all__ = ["calculations", "ceil", "Method"]

from lodash_python import _list, _string, _tuple, _number


class Method(Enum):
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"


def calculations(method_name: str, first: int, second: int):
    match method_name:
        case Method.ADD.value:
            return first + second
        case Method.SUBTRACT.value:
            return first - second
        case Method.MULTIPLY.value:
            return first * second
        case Method.DIVIDE.value:
            return first / second


def ceil(decimal: float):
    return math.ceil(decimal)


def math_functions():  # pragma: no cover
    add_result = calculations(Method.ADD.value, 1, 2)
    subtract_result = calculations(Method.SUBTRACT.value, 50, 30)
    multiply_result = calculations(Method.MULTIPLY.value, 50, 30)
    divide_result = calculations(Method.DIVIDE.value, 50, 10)
    ceil_result = ceil(3.11)

    print("Add Result = ", add_result)
    print("Subtract Result = ", subtract_result)
    print("Multiply Result = ", multiply_result)
    print("Divide Result = ", divide_result)
    print("Ceil Result = ", ceil_result)


if __name__ == "__main__":  # pragma: no cover
    print('--------****MATH****--------')
    math_functions()
    print('--------****LIST****--------')
    _list.list_functions()
    print('--------****STRING****--------')
    _string.string_functions()
    print('--------****NUMBER****--------')
    _number.number_function()
    print('--------****TUPLES****--------')
    _tuple.tuple_function()
