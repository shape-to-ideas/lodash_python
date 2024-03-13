__all__ = ["clamp", "number_function"]


def clamp(number: int, lower_limit: int, upper_limit: int):
    if number >= upper_limit:
        return upper_limit
    elif number < lower_limit:
        return lower_limit
    return number


def number_function():
    clamp_result = clamp(10, -5, 5)
    print("Clamp Result =", clamp_result)
