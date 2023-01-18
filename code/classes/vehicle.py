import random

class Vehicle:

    def __init__(self, car, orientation, col, row, length):
        self.car = car
        self.x = col
        self.y = row
        self.orientation = orientation
        self.length = length 
        self.location_vehicle()
        self.color_vehicle()

    # def location_vehicle(self):

    #     self.area = []

    #     for i in range(self.length):

    #         if self.orientation == "H":
    #             self.area.append((self.y, self.x))
    #             self.x += 1
            
    #         else:
    #             self.area.append((self.y, self.x))
    #             self.y += 1
    
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