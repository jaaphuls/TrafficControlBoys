import numpy as np
import pandas as pd
import random
import copy

from code.classes.vehicle import Vehicle

class Board:

    def __init__(self, cars, N):
        """
        Arguments: list with cars, board size N

        Creates the Rush Hour gameboard: an NxN numpy array

        """

        self.N = N
        self.rush_board = np.zeros((N, N), dtype=Vehicle)
        self.car_list = cars
        self.create_board()
        self.string_value = self.create_state()
        self.visualize()
    
    def create_board(self):
        """
        Puts the Vehicle objects in the right places

        """

        # loop through the Vehicle objects in the car list
        for car in self.car_list:

            # find the location of the current car
            x = car.x
            y = car.y

            # loop through the length to put the whole car on the board
            for coord in range(car.length):

                # put the car name on the board with the right coordinate
                self.rush_board[y, x] = car.car

                # update the coordinate in the correct direction
                if car.orientation == 'H':
                    x += 1
                else:
                    y += 1

    def create_state(self):
        """"
        Converts the Vehicle objects and the corresponding locations into a string:
        This is a computational efficient way to save the current board state

        Returns the string (total) that corresponds with the current gameboard state
        """


        # create an empty string and loop through the Vehicle objects in the car list
        total = ''
        for car in self.car_list:

            # convert the car name and the coordinates into strings
            auto = str(car.car)
            x = str(car.x)
            y = str(car.y)

            # add the car strings to the total
            auto = auto + x + y
            total += auto
        
        return total
            
    def check_move(self):
        """
        Finds all possible subsequent moves and puts them in a list with child nodes, and keeps track of the moves made

        Returns a list with all possible child nodes (possible_boards) and a list of the moves that were made (movement_list)

        """
        
        # initialize the two lists with all possible child nodes and moves that were made
        possible_boards = []
        movement_list = []
        
        # loop through the cars and their indices in the car list
        for index, car in enumerate(self.car_list):
            
            # only change the x-coordinates if the car is oriented horizontally
            if car.orientation == 'H':

                # find which coordinates are to the left and right side of the car
                x_left = (car.x - 1)
                x_right = (car.x + car.length)

                # create a variable to update the amount of steps to the left
                step_left = 1

                # check if the Vehicle can (still) make a move to the left
                while x_left >= 0 and self.rush_board[car.y, x_left] == '.':  

                    # create a deep copy of the car list to remain the current state                          
                    new_car_list = copy.deepcopy(self.car_list)

                    # find the same car in the new list and update its location
                    new_car = new_car_list[index]
                    new_car.x -= step_left

                    # update the coordinate/amount of steps to the left
                    x_left -= 1
                    step_left += 1
                    
                    # update both the lists that the function will return
                    possible_boards.append(new_car_list)
                    movement_list.append(((car.car), -1))

                # create a variable to update the amount of steps to the right
                step_right = 1

                # check if the Vehicle can (still) make a move to the right
                while x_right < self.N and self.rush_board[car.y, x_right] == '.': 

                    # create a deep copy of the car list to remain the current state 
                    new_car_list = copy.deepcopy(self.car_list)

                    # find the same car in the new list and update its location
                    new_car = new_car_list[index]
                    new_car.x += step_right

                    # update the coordinate/amount of steps to the right
                    x_right += 1
                    step_right += 1
                    
                    # update both the lists that the function will return
                    possible_boards.append(new_car_list) 
                    movement_list.append(((car.car), 1))                     

            # if the car orientation is not horizontal it must be vertical
            # this means that only the y-coordinates should be changed
            else:

                # find which coordinates are to the up and down side of the car
                y_up = (car.y - 1)
                y_down = (car.y + car.length)
                
                # create a variable to update the amount of steps down
                step_down = 1

                # check if the Vehicle can (still) make a move down
                while y_down < self.N and self.rush_board[y_down, car.x] == '.':

                    # create a deep copy of the car list to remain the current state 
                    new_car_list = copy.deepcopy(self.car_list)

                    # find the same car in the new list and update its location
                    new_car = new_car_list[index]
                    new_car.y += step_down

                    # update the coordinate/amount of steps down
                    y_down += 1
                    step_down += 1
                    
                    # update both the lists that the function will return
                    possible_boards.append(new_car_list) 
                    movement_list.append(((car.car), 1))
                
                # create a variable to update the amount of steps up
                step_up = 1

                # check if the Vehicle can (still) make a move up
                while y_up >= 0 and self.rush_board[y_up, car.x] == '.':

                    # create a deep copy of the car list to remain the current state 
                    new_car_list = copy.deepcopy(self.car_list)

                    # find the same car in the new list and update its location
                    new_car = new_car_list[index]
                    new_car.y -= step_up

                    # update the coordinate/amount of steps up
                    y_up -= 1
                    step_up += 1

                    # update both the lists that the function will return
                    possible_boards.append(new_car_list) 
                    movement_list.append(((car.car), -1))
                
        return possible_boards, movement_list


    ### deze functie kan weg als alles klaar is ###

    def visualize(self):
        possible_moves = []

        for row in range(len(self.rush_board)):
            for column in range(len(self.rush_board)):

                if self.rush_board[row, column] == 0:
                   possible_moves.append((row, column))
                   self.rush_board[row, column] = '.'
        # print(self.rush_board)
        return self.rush_board
