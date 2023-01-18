import random

class Vehicle:

    def __init__(self, car, orientation, col, row, length):
        self.car = car
        self.x = col
        self.y = row
        self.orientation = orientation
        self.length = length 