
from code.classes.vehicle import Vehicle
from code.classes.board import Board
import pandas as pd
import argparse
import random
import matplotlib.pyplot as plt
import numpy as np
from code.algorithms.random import Random

# this code block asks for a user input and keeps asking untill a good input is given
while True:
    board_size = input("What are the board dimensions (6x6, 9x9 or 12x12)? \n")
    if board_size not in ('6', '9', '12', '6x6', '9x9', '12x12'):
        print("There are no boards with these dimensions, please chose the correct dimensions!")
    else:
        break

if board_size == '6' or board_size == '6x6':
    board_size = 6 
    game_number = int(input('Which game would you like to play? \n Enter 1 for game 1 \n Enter 2 for game 2 \n Enter 3 for game 3 \n Enter 4 for game 4 \n'))

    if game_number == 1: 
        csv_rh = 'data/Rushhour6x6_1.csv'
    elif game_number == 2: 
        csv_rh = 'data/Rushhour6x6_2.csv'
    elif game_number == 3: 
        csv_rh = 'data/Rushhour6x6_3.csv'
    elif game_number == 4: 
        csv_rh = 'data/Rushhour6x6_4.csv'

elif board_size == '9' or board_size == '9x9': 
    board_size = 9
    game_number = int(input('Which game would you like to play? \n Enter 1 for game 4 \n Enter 2 for game 5 \n Enter 3 for game 6 \n'))

    if game_number == 1: 
        csv_rh = 'data/Rushhour9x9_4.csv'
    elif game_number == 2: 
        csv_rh = 'data/Rushhour9x9_5.csv'
    elif game_number == 3: 
        csv_rh = 'data/Rushhour9x9_6.csv'

elif board_size == '12' or board_size == '12x12':
    board_size = 12 
    game_number = int(input('Which game would you like to play? \n Enter 1 for game 1 \n'))

    if game_number == 1: 
        csv_rh = 'data/Rushhour12x12_7.csv'


# read the csv input file as a pandas dataframe
dataframe = pd.read_csv(csv_rh)

# loop through the indices and rows of the car positions dataframe
car_list = []

for i, row in dataframe.iterrows():
    car_list.append(Vehicle(row['car'], row['orientation'], row['col'], row['row'], row['length']))

# Run main with provide arguments
board = Board(car_list, board_size)

while board.rush_board[2, 5] != "X":
     #board = Board(car_list, board_size)
    board.create_state()
    board.create_board()
    board.check_move()

    print(board.rush_board[2, 5])

    car_list = Random.random_step(board)
    board = Board(car_list, board_size)
    
    print("")

# board.create_state()
# board.create_board()
# board.check_move()