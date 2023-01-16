from code.visualisation.visualise import gameboard as gb 
from code.classes.vehicle import Vehicle
from code.classes.board import create_board
import pandas as pd
import argparse
import random
import matplotlib.pyplot as plt
import numpy as np

parser = argparse.ArgumentParser()

# Adding arguments
parser.add_argument("input", help = "input file (csv)")

# Read arguments from command line
args = parser.parse_args()

# read the csv input file as a pandas dataframe
dataframe = pd.read_csv(args.input)

# loop through the indices and rows of the car positions dataframe
car_list = []

for i, row in dataframe.iterrows():
    car_list.append(Vehicle(row['car'], row['orientation'], row['col'], row['row'], row['length']))

# Run main with provide arguments
board_visualized = gb(car_list, 6)

board = create_board(car_list)
board.create_state()
