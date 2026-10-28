def equilateral(sides):
    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False
    elif not (sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]):
        return False
    else:
        return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False
    elif not (sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]):
        return False
    else:
        return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]


def scalene(sides):
    if sides[0] <= 0 or sides[1] <= 0 or sides[2] <= 0:
        return False
    elif not (sides[0] + sides[1] > sides[2] and sides[0] + sides[2] > sides[1] and sides[1] + sides[2] > sides[0]):
        return False
    else:
        return (sides[0] != sides[1]) and (sides[1] != sides[2]) and (sides[0] != sides[2])