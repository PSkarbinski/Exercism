def is_armstrong_number(number: int) -> bool:
    numbersList = list[str](str(number))
    numbersListLength = len(numbersList)
    result: int = 0
    for i in range(numbersListLength):
        val = int(numbersList[i])
        result += val ** numbersListLength
        
    return result == number