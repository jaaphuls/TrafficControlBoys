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
                #print(f'this is temp_area {temp_area}')
                check_x_left = (car.y, (temp_area[0][1])-1)
                check_x_right = (car.y, (temp_area[-1][1])+1)
                #print(f'this is check_x_left {check_x_left}')
                #print(f'this is check_x_right {check_x_right}')

            elif car.orientation == "V":
                temp_area = car.area
                print(f'this is temp_area {temp_area}')
                check_y_up = ((temp_area[0][0])-1, car.x)
                check_y_down = ((temp_area[-1][1])+1, car.x)
                print(f'this is check_y_up {check_y_up}')
                print(f'this is check_y_down {check_y_down}')


    def is_solved(self): 

        correct_x = self.N + 2
        for car in self.car_list: 
            if car.car == 'X' and car.x == correct_x: 
                return True
        
        return False

                
      