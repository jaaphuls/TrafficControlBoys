import numpy as np
import pandas as pd
import random

from code.classes.vehicle import Vehicle

class Board:

    def __init__(self, cars, N):
        self.N = N
        self.rush_board = np.zeros((N, N), dtype=Vehicle)
        self.car_list = cars
        self.states_list = []

    def create_state(self):
        # state = []
        
        for car in self.car_list:

            state = [car.car, car.x, car.y]
            
            self.states_list.append(state)

    def create_board(self):

            for car in self.car_list:
                x = car.x
                y = car.y
                for coord in range(car.length):
                    self.rush_board[y, x] = car.car

                    if car.orientation == 'H':
                        x += 1
                    else:
                        y += 1  
    
    def visualize(self):
        possible_moves = []

        for row in range(len(self.rush_board)):
            for column in range(len(self.rush_board)):

                if self.rush_board[row, column] == 0:
                   possible_moves.append((row, column))
                   self.rush_board[row, column] = '.'
        
        return self.rush_board    
    
    def visualize(self):
        possible_moves = []

        for row in range(len(self.rush_board)):
            for column in range(len(self.rush_board)):

                if self.rush_board[row, column] == 0:
                   possible_moves.append((row, column))
                   self.rush_board[row, column] = '.'
        
        return self.rush_board

    def check_move(self):
        possible_boards = []

        for car in self.car_list:
            if car.orientation == 'H': 
                x_left = (car.x - 1)
                x_right = (car.x + car.length)
            
                while x_left >= 0 and self.rush_board[car.y, x_left] == '.': 
                    new_car_list = self.car_list.copy()
                    new_car = Vehicle(car.car, car.orientation, x_left + 1, car.y+1, car.length)

                    new_car_list.remove(car)
                    new_car_list.append(new_car)

                    possible_boards.append(new_car_list)
                    
                    if x_left > 0:
                        x_left -= 1

                    else:
                        break

                while x_right < self.N and self.rush_board[car.y, x_right] == '.':
                    new_car_list = self.car_list.copy()
                    new_car = Vehicle(car.car, car.orientation, x_right - car.length + 1, car.y+1, car.length)

                    print(f'x_right: {x_right}')

                    new_car_list.remove(car)
                    new_car_list.append(new_car)

                    possible_boards.append(new_car_list)

                    if (x_right + 1) < self.N:
                        x_right += 1
                 
                    else:
                        break
                        
            else:
                y_down = (car.y + car.length)
                y_up = (car.y - 1)
        
                while y_down < self.N and self.rush_board[y_down, car.x] == '.':
                    new_car_list = self.car_list.copy()
                    new_car = Vehicle(car.car, car.orientation, car.x+1, y_down - car.length + 1, car.length)

                    new_car_list.remove(car)
                    new_car_list.append(new_car)

                    possible_boards.append(new_car_list)

                    if (y_down + 1) < self.N:
                        y_down += 1
                    else:
                        break

                while y_up >= 0 and self.rush_board[y_up, car.x] == '.':
                    new_car_list = self.car_list.copy()
                    new_car = Vehicle(car.car, car.orientation, car.x+1, y_up + 1, car.length)
                    

                    new_car_list.remove(car)
                    new_car_list.append(new_car)

                    possible_boards.append(new_car_list)

                    if y_up > 0:
                        y_up -= 1
                    else:
                        break

                
        return possible_boards
    
    
    def visualize(self):
        possible_moves = []

        for row in range(len(self.rush_board)):
            for column in range(len(self.rush_board)):

                if self.rush_board[row, column] == 0:
                   possible_moves.append((row, column))
                   self.rush_board[row, column] = '.'

        print(self.rush_board)

        return self.rush_board

