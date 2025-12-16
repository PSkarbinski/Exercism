def is_armstrong_number(number: int) -> bool:
    numberStr = str(number)
    result: int = 0
    for i in numberStr:
        result += int(i) ** len(numberStr)
    return result == number