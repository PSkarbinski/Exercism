def score(x: int | float, y: int | float) -> int:
    posSquared = x ** 2 + y ** 2
    innerRadiusSquared = 1 ** 2
    middleRadiusSquared = 5 ** 2
    outerRadiusSquared = 10 ** 2
    
    return 10 if posSquared <= innerRadiusSquared else 5 if posSquared <= middleRadiusSquared else 1 if posSquared <= outerRadiusSquared else 0
