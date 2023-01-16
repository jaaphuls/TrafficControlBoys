import numpy as np
import pandas as pd
import random

from code.classes.vehicle import Vehicle


class create_board:

    def __init__(self, cars, N=6,):
        self.rush_board = np.zeros((N + 2, N + 2), dtype=Vehicle)
        self.car_list = cars
       
    def create_state(self):

        for car in self.car_list:
            # print(car.area)
            for coordinate in car.area:
                print(coordinate)

            
                # self.rush_board = self.rush_board[car.area]
    

    def random_step(self): 

        car = random.choice(self.car_list)

        # check in what orientation the car should move
        if car.orientation == 'H': 

            # give a chance of 0.5 to either move towards the right or left
            if random.randint(1, 2) != 1:
                if gameboard[car.x + 1, car.y] == [1, 1, 1]:  
                    car.x += 1 
            else: 
                if gameboard[car.x - 1, car.y] == [1, 1, 1]:  
                    car.x -= 1
        
        # if the orientation is not horizontal, move on the y-axis
        else: 

            # give the same chance of 0.5 to move towards the top or the bottom
            if random.randint(1, 2) != 1: 
                if gameboard[car.x, car.y + 1] == [1, 1, 1]:
                    car.y += 1 
            else: 
                if gameboard[car.x, car.y - 1] == [1, 1, 1]:
                    car.y -= 1

        
      