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
                #print(coordinate)
                pass
            
                # self.rush_board = self.rush_board[car.area]


    def check_move(self):

        for car in self.car_list:

            # check in what orientation the car should move
            if car.orientation == 'H': 

                if gameboard[car.x + 1, car.y] == [1, 1, 1]:  
                    return True 

                elif gameboard[car.x - 1, car.y] == [1, 1, 1]:  
                    return True
            
            # if the orientation is not horizontal, move on the y-axis
            else: 

                # give the same chance of 0.5 to move towards the top or the bottom
                if gameboard[car.x, car.y + 1] == [1, 1, 1]:
                    return True
     
                elif gameboard[car.x, car.y - 1] == [1, 1, 1]:
                    return True

        return False


    def is_solved(self): 

        correct_x = self.N + 2
        for car in self.car_list: 
            if car.car == 'X' and car.x == correct_x: 
                return True
        
        return False

                
      