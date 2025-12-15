def square(number: int) -> int:
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    result = 1
    i = 1
    while i < number:
        result = result * 2
        i = i + 1
    return result


def total() -> int:
    total = 0
    i = 1
    while i < 65:
        total = total + square(i)
        i = i + 1
    return total
