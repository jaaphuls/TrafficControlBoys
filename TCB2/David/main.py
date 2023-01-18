import pandas as pd
import numpy as np
from board import Board
from vehicle import Vehicle

csv = 'data/Rushhour6x6_4.csv'

# read the csv input file as a pandas dataframe
dataframe = pd.read_csv(csv)

board = Board(9)

for i, row in dataframe.iterrows():
    car = Vehicle(row['car'], row['orientation'], row['length'])

    x = row['col']
    y = row['row']

    board.initialize_car(car, x, y)

print(board.rush_board)