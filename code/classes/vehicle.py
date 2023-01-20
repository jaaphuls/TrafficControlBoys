import random

class Vehicle:

    def __init__(self, car, orientation, col, row, length):
        self.car = car
        self.x = col -1
        self.y = row -1
        self.orientation = orientation
        self.length = length 
        
    #     self.color_vehicle()
    
    # def color_vehicle(self):

    #     if self.car == 'X':
    #         r, g, b = 1, 0, 0

    #     else:

    #         # create random color values
    #         # the red value is limited to prevent red cars from appearing
    #         r = random.uniform(0,0.7)
            
    #         # cars with different lengths are given a slightly different color
    #         if self.length == 2:
    #             g = random.uniform(0,0.8)
    #             b = random.random()

    #         else:
    #             g = random.random()
    #             b = random.uniform(0,0.8)
    
    #     self.color = [r, g, b]