import numpy as np
import pandas as pd
import random
import copy

from vehicle import Vehicle

class Board:

    def __init__(self, N):
        self.rush_board = np.zeros((N, N), dtype=Vehicle)

    def initialize(self, vehicle, x, y):

        for i in range(vehicle.length):

            if vehicle.orientation == "H":
                self.rush_board[y, x] = vehicle
                self.occupied.add((y, x))
                x += 1
            
            else:
                self.rush_board[y, x] = vehicle
                self.occupied.add((y, x))
                y += 1

    def update_car(self, x, y, backwards=False):

        car = self.rush_board[y, x]

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

    def visualize(self):
        visualized = copy.copy(self.rush_board)
        for y, row in enumerate(visualized):
            for x, coord in enumerate(row):
                if type(coord) == Vehicle:
                   visualized[y,x] = coord.car

                else:
                    visualized[y,x] = '.'

        print(visualized)


