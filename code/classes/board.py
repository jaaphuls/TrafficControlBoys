import numpy as np
import pandas as pd
import random

from code.classes.vehicle import Vehicle

class create_board:

    def __init__(self, cars, N=6):
        self.N = N 
        self.rush_board = np.zeros((N + 2, N + 2), dtype=Vehicle)
        self.car_list = cars
       
    def create_state(self):
        self.car_dict = {}

        for car in self.car_list:
            # print(car.area)
            for coordinate in car.area:
                self.rush_board[(coordinate)] = car
                car_dict[coordinate] = car

    def check_move(self, car):
        
        # check the orientation of the car and if the car is able to move
        if car.orientation == 'H': 
            check_x_left = (car.y, (car.area[0][1])-1)

            check_x_right = (car.y, (car.area[-1][1])+1)

        elif car.orientation == "V":
            check_y_up = ((car.area[0][0])-1, car.x)
            check_y_down = ((car.area[-1][0])+1, car.x)

    def is_solved(self): 

        correct_x = self.N + 2
        for car in self.car_list: 
            if car.car == 'X' and car.x == correct_x: 
                return True
        
        return False

                
      