'''Calculate the number of grains of wheat on a chessboard.

A chessboard has 64 squares. Square 1 has one grain, square 2 has two grains, square 3 has four grains, and so on, doubling each time.

Write code that calculates:

the number of grains on a given square
the total number of grains on the chessboard'''

def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        return 2 ** (number - 1)

def total():
    sum = 0
    for num in range(1,65):
        sum += square(num)
    return sum

C:\Users\prasa\Python_Learning\Day_02\grains.py