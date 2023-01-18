import pandas as pd
import numpy as np
from board import Board
from vehicle import Vehicle

csv = 'data/Rushhour6x6_1.csv'

# read the csv input file as a pandas dataframe
dataframe = pd.read_csv(csv)

board = Board(6)

for i, row in dataframe.iterrows():
    car = Vehicle(row['car'], row['orientation'], row['length'])

    x = row['col'] - 1
    y = row['row'] - 1

    board.initialize(car, x, y)

updates = [(1,0), (1,1), (2,2), (2,1), (4,4), (5,2)]
booleans = [True, True, True, True, True, False]

for update, boolean in zip(updates, booleans):
    x, y = update
    board.update_car(x, y, backwards=boolean)
    board.visualize()


