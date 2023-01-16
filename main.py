from code.visualisation.visualise import gameboard as gb 
from code.classes.vehicle import Vehicle
from code.classes.board import create_board
import pandas as pd
import argparse
import random
import matplotlib.pyplot as plt
import numpy as np


board_size = int(input('What are the board dimensions? \n'))

if board_size == 6: 
    game_number = int(input(' Enter 1 for game 1 \n Enter 2 for game 2 \n Enter 3 for game 3 \n'))

    if game_number == 1: 
        csv_rh = 'data/Rushhour6x6_1.csv'
    elif game_number == 2: 
        csv_rh = 'data/Rushhour6x6_2.csv'
    elif game_number == 3: 
        csv_rh = 'data/Rushhour6x6_3.csv'

elif board_size == 9: 
    game_number = int(input(' Enter 1 for game 4 \n Enter 2 for game 5 \n Enter 3 for game 6 \n'))

    if game_number == 1: 
        csv_rh = 'data/Rushhour9x9_4.csv'
    elif game_number == 2: 
        csv_rh = 'data/Rushhour9x9_5.csv'
    elif game_number == 3: 
        csv_rh = 'data/Rushhour9x9_6.csv'

elif board_size == 12: 
    game_number = int(input(' Enter 1 for game 1 \n'))

    if game_number == 1: 
        csv_rh = 'data/Rushhour12x12_7.csv'


# read the csv input file as a pandas dataframe
dataframe = pd.read_csv(csv_rh)

# loop through the indices and rows of the car positions dataframe
car_list = []

for i, row in dataframe.iterrows():
    car_list.append(Vehicle(row['car'], row['orientation'], row['col'], row['row'], row['length']))

# Run main with provide arguments
board_visualized = gb(car_list, board_size)

board = create_board(car_list)
board.create_state()
board.check_move()
