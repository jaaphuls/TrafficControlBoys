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

        for car in self.car_list:
            # print(car.area)
            for coordinate in car.area:
                self.rush_board[(coordinate)] = car


    def check_move(self):

        for car in self.car_list:

            # check in what orientation the car should move
            if car.orientation == 'H': 
                temp_area = car.area
                temp_x = (car.y, (temp_area[0][0])+1)
                print(temp_x)


    def is_solved(self): 

        correct_x = self.N + 2
        for car in self.car_list: 
            if car.car == 'X' and car.x == correct_x: 
                return True
        
        return False

                
      