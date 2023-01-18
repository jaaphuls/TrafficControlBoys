import numpy as np
import pandas as pd
import random

from code.classes.vehicle import Vehicle

class Board:

    def __init__(self, cars, N=6):
        self.N = N 
        self.car_dict = self.borders(N)
        self.rush_board = np.zeros((N + 2, N + 2), dtype=Vehicle)
        self.car_list = cars
        self.states_list = []
    
    def borders(self, N):

        borders = {}

        for x in range(N + 2):
            borders[0, x] = 'border'
            borders[N + 1, x] = 'border'

        for y in range(N + 2):
            borders[y, 0] = 'border'
            borders[y, N + 1] = 'border'
        
        return borders

    def create_state(self):
        state = []
        for car in vehicle.car:
            if car.orientation == 'H' and car.length == '2':
                state.append(car.car, car.x, car.y, car.x + 1, car.y)
             
            elif car.orientation == 'H' and car.length == '3':
                state.append(car.car, car.x, car.y, car.x + 2, car.y)
            
            elif car.orientation == 'V' and car.length == '2':
                state.append(car.car, car.x, car.y, car.x, car.y + 1)

            elif car.orientation == 'V' and car.length == '3':
                state.append(car.car, car.x, car.y, car.x, car.y + 2)
    
        self.states_list.append(state)

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

                
      
