def isTriangle(sides: list[float]) -> bool:
    return 0 not in sides and sides[0] + sides[1] >= sides[2] and sides[0] + sides[2] >= sides[1] and sides[1] + sides[2] >= sides[0]

def equilateral(sides: list[float]) -> bool:
    return isTriangle(sides) and sides[0] == sides[1] and sides[1] == sides[2]

def isosceles(sides: list[float]) -> bool:
    return isTriangle(sides) and (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2])

def scalene(sides: list[float]) -> bool:
    return isTriangle(sides) and sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]
