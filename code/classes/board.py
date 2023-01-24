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
            for index, car in enumerate(self.car_list):
                
                if car.orientation == 'H': 
                    x_left = (car.x - 1)
                    x_right = (car.x + car.length)
                
                    if x_left >= 0 : 
                        if self.rush_board[car.y, x_left] == '.':
                            new_car_list = copy.deepcopy(self.car_list)

                            new_car_list[index].x = x_left
                            
                            possible_boards.append(new_car_list)

                    if x_right - 1 != self.N - 1: 
                        if self.rush_board[car.y, x_right] == '.':
                            new_car_list = copy.deepcopy(self.car_list)

                            new_car_list[index].x += 1

                            possible_boards.append(new_car_list)
                            
                            
                else:
                    y_down = (car.y + car.length)
                    y_up = (car.y - 1)
        
                    if y_down - 1 != self.N - 1:
                        if self.rush_board[y_down, car.x] == '.':
                            new_car_list = copy.deepcopy(self.car_list)
                        

                            
                            new_car_list[index].y += 1

                            possible_boards.append(new_car_list)

                    if y_up >=  0:
                        if self.rush_board[y_up, car.x] == '.':
                            new_car_list = copy.deepcopy(self.car_list)
                            
                            new_car_list[index].y = y_up

                            possible_boards.append(new_car_list)
        
            return possible_boards

    # def check_move(self):
    #     possible_boards = []
    #     for car in self.car_list:

    #         if car.orientation == 'H': 
    #             x_left = (car.x - 1)
    #             x_right = (car.x + car.length)
    #             # x_left_2 = (car.x - 2)
    #             # x_right_2 = (car.x + car.length + 1)
            
    #             if x_left >= 0 : 
    #                 if self.rush_board[car.y, x_left] == '.':
    #                     new_car_list = self.car_list.copy()
    #                     new_car = Vehicle(car.car, car.orientation, car.x, car.y+1, car.length)
    #                     new_car.color = car.color
    #                     new_car_list.remove(car)
    #                     new_car_list.append(new_car)

    #                     possible_boards.append(new_car_list)

    #             # if x_left_2 >= 0:
    #             #     if self.rush_board[car.y, x_left_2] == '.' and self.rush_board[car.y, x_left] == '.':
    #             #         new_car_list = self.car_list.copy()
    #             #         new_car = Vehicle(car.car, car.orientation, car.x - 1, car.y+1, car.length)
    #             #          new_car.color = car.color
    #             #         new_car_list.remove(car)
    #             #         new_car_list.append(new_car)

    #             #         possible_boards.append(new_car_list)

    #             if x_right - 1 != self.N - 1: 
    #                 if self.rush_board[car.y, x_right] == '.':
    #                     new_car_list = self.car_list.copy()
    #                     new_car = Vehicle(car.car, car.orientation, car.x+2, car.y+1, car.length)
    #                     new_car.color = car.color
    #                     new_car_list.remove(car)
    #                     new_car_list.append(new_car)

    #                     possible_boards.append(new_car_list)
                
    #             # if x_right_2 - 1 < self.N - 1: 
    #             #     if self.rush_board[car.y, x_right_2] == '.' and self.rush_board[car.y, x_right] == '.':
    #             #         new_car_list = self.car_list.copy()
    #             #         new_car = Vehicle(car.car, car.orientation, car.x + 3, car.y+1, car.length)
    #             #         new_car.color = car.color
    #             #         new_car_list.remove(car)
    #             #         new_car_list.append(new_car)

    #             #         possible_boards.append(new_car_list)
                        
                        
    #         else:
    #             y_down = (car.y + car.length)
    #             y_up = (car.y - 1)
    #             # y_down_2 = (car.y + car.length + 1)
    #             # y_up_2 = (car.y - 2)
        
    #             if y_down - 1 != self.N - 1:
    #                 if self.rush_board[y_down, car.x] == '.':
    #                     new_car_list = self.car_list.copy()
    #                     new_car = Vehicle(car.car, car.orientation, car.x+1, car.y+2, car.length)
    #                     new_car.color = car.color
    #                     new_car_list.remove(car)
    #                     new_car_list.append(new_car)

    #                     possible_boards.append(new_car_list)
                
    #             # if y_down_2 - 1 < self.N - 1: 
    #             #     if self.rush_board[y_down_2, car.x] == '.' and self.rush_board[y_down, car.x] == '.':
    #             #         new_car_list = self.car_list.copy()
    #             #         new_car = Vehicle(car.car, car.orientation, car.x+1, car.y+3, car.length)
    #             #         new_car.color = car.color

    #             #         new_car_list.remove(car)
    #             #         new_car_list.append(new_car)

    #             #         possible_boards.append(new_car_list)

    #             if y_up >=  0:
    #                 if self.rush_board[y_up, car.x] == '.':
    #                     new_car_list = self.car_list.copy()
    #                     new_car = Vehicle(car.car, car.orientation, car.x+1, car.y, car.length)
    #                     new_car.color = car.color

    #                     new_car_list.remove(car)
    #                     new_car_list.append(new_car)

    #                     possible_boards.append(new_car_list)
                
    #             # if y_up_2 >= 0: 
    #             #     if self.rush_board[y_up_2, car.x] == '.' and self.rush_board[y_up, car.x] == '.':
    #             #         new_car_list = self.car_list.copy()
    #             #         new_car = Vehicle(car.car, car.orientation, car.x+1, car.y - 1, car.length)
    #             #         new_car.color = car.color

    #             #         new_car_list.remove(car)
    #             #         new_car_list.append(new_car)

    #             #         possible_boards.append(new_car_list)               

                
    #     return possible_boards
    
    
    def visualize(self):
        possible_moves = []

        for row in range(len(self.rush_board)):
            for column in range(len(self.rush_board)):

                if self.rush_board[row, column] == 0:
                   possible_moves.append((row, column))
                   self.rush_board[row, column] = '.'
        print(self.rush_board)
        return self.rush_board

