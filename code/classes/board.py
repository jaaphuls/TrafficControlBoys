import numpy as np
import pandas as pd
import random
import copy

from code.classes.vehicle import Vehicle

class Board:

    def __init__(self, cars, N):
        self.N = N
        self.rush_board = np.zeros((N, N), dtype=Vehicle)
        self.car_list = cars
        self.states_list = set()
        self.string_value = self.create_state()


    def create_state(self):
        total = ''
        for car in self.car_list:
            auto = str(car.car)
            x = str(car.x)
            y = str(car.y)

            auto = auto + x + y
            total += auto
        
        return total
    
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
            
    def check_move(self):
        possible_boards = []
        movement_list = []
        
        for index, car in enumerate(self.car_list):
            
            if car.orientation == 'H': 
                x_left = (car.x - 1)
                x_right = (car.x + car.length)

                step_left = 1
                while x_left >= 0 and self.rush_board[car.y, x_left] == '.':                            
                    new_car_list = copy.deepcopy(self.car_list)

                    new_car = new_car_list[index]

                    new_car.x -= step_left
                    step_left += 1
                    x_left -= 1
                    
                    possible_boards.append(new_car_list)
                    movement_list.append(((car.car), -1))
                                
                step_right = 1
                while x_right < self.N and self.rush_board[car.y, x_right] == '.': 
                    new_car_list = copy.deepcopy(self.car_list)

                    new_car = new_car_list[index]

                    new_car.x += step_right
                    x_right += 1
                    step_right += 1
                    
                    possible_boards.append(new_car_list) 
                    movement_list.append(((car.car), 1))                     
                        
            else:
                y_down = (car.y + car.length)
                y_up = (car.y - 1)
                
                step_down = 1
                while y_down < self.N and self.rush_board[y_down, car.x] == '.':
                    new_car_list = copy.deepcopy(self.car_list)

                    new_car = new_car_list[index]

                    new_car.y += step_down
                    y_down += 1
                    step_down += 1
                    
                    possible_boards.append(new_car_list) 
                    movement_list.append(((car.car), 1))
                
                step_up = 1
                while y_up >= 0 and self.rush_board[y_up, car.x] == '.':
                    new_car_list = copy.deepcopy(self.car_list)

                    new_car = new_car_list[index]

                    new_car.y -= step_up
                    y_up -= 1
                    step_up += 1
                    
                    possible_boards.append(new_car_list) 
                    movement_list.append(((car.car), -1))
                
        return possible_boards, movement_list

    def visualize(self):
        possible_moves = []

        for row in range(len(self.rush_board)):
            for column in range(len(self.rush_board)):

                if self.rush_board[row, column] == 0:
                   possible_moves.append((row, column))
                   self.rush_board[row, column] = '.'
        # print(self.rush_board)
        return self.rush_board
