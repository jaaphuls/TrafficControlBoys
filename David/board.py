import numpy as np
import pandas as pd
import random

from vehicle import Vehicle

class Board:

    def __init__(self, N):
        self.occupied = self.borders(N)
        self.rush_board = np.zeros((N + 2, N + 2), dtype=Vehicle)
    
    def borders(self, N):

        borders = set()

        for x in range(N + 2):
            borders.add((0, x))
            borders.add((N + 1, x))

        for y in range(N + 2):
            borders.add((y, 0))
            borders.add((y, N + 1))
        
        return borders

    def initialize_car(self, vehicle, x, y):

        for i in range(vehicle.length):

            if vehicle.orientation == "H":
                self.rush_board[y, x] = vehicle.car
                self.occupied.add((y, x))
                x += 1
            
            else:
                self.rush_board[y, x] = vehicle.car
                self.occupied.add((y, x))
                y += 1

    def update_car(self, x, y, car, backwards):

        car_front = car.length - 1

        if car.orientation == 'H':

            if backwards:
                self.rush_board[y, x + car_front] = 0
                self.rush_board[y, x - 1] = car

            else:
                self.rush_board[y, x] = 0
                self.rush_board[y, x + car.length] = car

        else:
            if backwards:
                self.rush_board[y + car_front, x] = 0
                self.rush_board[y - 1, x] = car

            else:
                self.rush_board[y, x] = 0
                self.rush_board[y + car.length, x] = car


