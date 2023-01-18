import numpy as np
import pandas as pd
import random

from code.classes.vehicle import Vehicle

class Board:

    def __init__(self, cars, N):
        self.N = N
        self.rush_board = np.zeros((N , N ), dtype=Vehicle)
        self.car_list = cars
        self.states_list = []

    def create_state(self):
        state = []
        for car in self.car_list:
            orientation = car.orientation
            length = car.length
            x = car.x
            y = car.y
            if car.orientation == 'H' and car.length == 2:
                state.append((car.car, car.length, car.x, car.y, car.x + 1, car.y))
             
            elif car.orientation == 'H' and car.length == 3:
                state.append((car.car, car.length, car.x, car.y, car.x + 1, car.y, car.x + 2, car.y))
            
            elif car.orientation == 'V' and car.length == 2:
                state.append((car.car, car.length, car.x, car.y, car.x, car.y + 1))

            elif car.orientation == 'V' and car.length == 3:
                state.append((car.car, car.length, car.x, car.y, car.x, car.y + 1, car.x, car.y + 2))
    
        self.states_list.append(state)

    def create_board(self):

        for state in self.states_list:
            for car in state:
                if car[1] == 2:
                    self.rush_board[(car[3]-1, car[2]-1)] = car[0]
                    self.rush_board[(car[5]-1, car[4]-1)] = car[0]
                if car[1] == 3:
                    self.rush_board[(car[3]-1, car[2]-1)] = car[0]
                    self.rush_board[(car[5]-1, car[4]-1)] = car[0]
                    self.rush_board[(car[7]-1, car[6]-1)] = car[0]
       
    def check_move(self):
        possible_moves = []

        for row in range(len(self.rush_board)):
            for column in range(len(self.rush_board)):
                if self.rush_board[row, column] == 0:
                   possible_moves.append((row, column))

        for i in possible_moves:
            self.rush_board[i] = '.'

        print(self.rush_board)
        return possible_moves