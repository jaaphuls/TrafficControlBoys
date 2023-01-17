import numpy as np
import pandas as pd
import random

from code.classes.vehicle import Vehicle

class Board:

    def __init__(self, cars, N=6):
        self.N = N 
        self.rush_board = np.zeros((N + 2, N + 2), dtype=Vehicle)
        self.car_list = cars
       
    def create_state(self):
        self.car_dict = {(0,0) :'border', (0,1) :'border', (0,2) : 'border', (0,3) : 'border', (0,4) : 'border', (0,5) : 'border', (0,6) : 'border', (0,7) : 'border',
        (1,7) : 'border', (2,7) : 'border', (3,7) : 'border', (4,7) : 'border', (5,7) : 'border', (6,7) : 'border', (7,7) : 'border',
        (7,1) : 'border', (7,2) : 'border', (7,3) : 'border', (7,4) : 'border', (7,5) : 'border', (7,6) : 'border', (7,7) : 'border',
        (6,7) : 'border', (5,7) : 'border', (4,7) : 'border', (2,7) : 'border', (1,7) : 'border', (0,7) : 'border'}

        for car in self.car_list:
            print(car.area)
            for coordinate in car.area:
                self.rush_board[(coordinate)] = car
                self.car_dict[coordinate] = car

    def check_move(self, car):

        # check the orientation of the car and if the car is able to move
        if car.orientation == 'H': 
            check_x_left = (car.y, (car.area[0][1])-1)
            check_x_right = (car.y, (car.area[-1][1])+1)

            if check_x_left not in self.car_dict.keys() and check_x_right not in self.car_dict.keys():
                return True, True

            elif check_x_left not in self.car_dict.keys() and check_x_right in self.car_dict.keys():
                return True, False
            
            elif check_x_left in self.car_dict.keys() and check_x_right not in self.car_dict.keys():
                return False, True

            elif check_x_left in self.car_dict.keys() and check_x_right in self.car_dict.keys():
                return False, False

        elif car.orientation == "V":
            check_y_up = ((car.area[0][0])-1, car.x)
            check_y_down = ((car.area[-1][0])+1, car.x)

            if check_y_up not in self.car_dict.keys() and check_y_down not in self.car_dict.keys():
                return True, True

            elif check_y_up not in self.car_dict.keys() and check_y_down in self.car_dict.keys():
                return True, False
            
            elif check_y_up in self.car_dict.keys() and check_y_down not in self.car_dict.keys():
                return False, True

            elif check_y_up in self.car_dict.keys() and check_y_down in self.car_dict.keys():
                return False, False

    def is_solved(self): 

        correct_x = self.N + 2
        for car in self.car_list: 
            if car.car == 'X' and car.x == correct_x: 
                return True
        
        return False

                
      