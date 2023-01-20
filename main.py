
from code.classes.vehicle import Vehicle
from code.classes.board import Board
from code.visualisation.visualise import gameboard
import pandas as pd
import argparse
import random
import matplotlib.pyplot as plt
import numpy as np
from code.algorithms.random_algo import random_step
import time

# this code block asks for a user input and keeps asking until a good input is given
board_size = None

while type(board_size) != int:
    dimensions = {'6x6' : '6', '9x9' : '9', '12x12' : '12'}
    
    board_size = input("What are the board dimensions (6x6, 9x9 or 12x12)? \n")
    
    if board_size in dimensions:
        board_size = int(dimensions[board_size])
    
    elif board_size in dimensions.values():
        board_size = int(board_size)

    else:
        print("There are no boards with these dimensions, please choose the correct dimensions!")

game_number = int(input('Which game would you like to play? \n Enter game number \n'))
    
csv_rh = (f'data/Rushhour{board_size}x{board_size}_{game_number}.csv')

# read the csv input file as a pandas dataframe
dataframe = pd.read_csv(csv_rh)

# loop through the indices and rows of the car positions dataframe
car_list = []

for i, row in dataframe.iterrows():
    car_list.append(Vehicle(row['car'], row['orientation'], row['col'], row['row'], row['length']))

# Run main with provide arguments
board = Board(car_list, board_size)
board.create_state()
board.create_board()
board.visualize()
new_car_list = random_step(board, board_size)



#board.check_move()
step = 0


