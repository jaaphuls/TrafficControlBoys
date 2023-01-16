import numpy as np
import pandas as pd

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
    
    def step(self, car_id): 

        for car in self.car_list: 
            if car_id == car.car: 
                if car.orientation == 'H': 
                    car.x += 1
                else: 
                    car.y += 1


        
      