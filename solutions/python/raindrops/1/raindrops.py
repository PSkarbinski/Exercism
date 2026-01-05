def convert(number: int) -> str:
    result = ''
    divByThree = number % 3 == 0
    divByFive = number % 5 == 0
    divBySeven = number % 7 == 0

    if (not (divByThree or divByFive or divBySeven)):
        result = str(number)
    else:
        if (divByThree):
            result = result + 'Pling'
        if (divByFive):
            result = result + 'Plang'
        if (divBySeven):
            result = result + 'Plong'

    return result