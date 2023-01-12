import pandas as pd
import argparse
import random
import matplotlib.pyplot as plt
import numpy as np

def gameboard(input_filename):
    """
    Arguments: csv input filename with car positions
    
    Creates an NxN gameboard with a black edge and colored cars

    Returns the Rush Hour gameboard
    """
    
    # read the csv input file as a pandas dataframe
    dataframe = pd.read_csv(input_filename)
    
    # find the width and height N of the gameboard
    # the slicing is corrected for N > 9
    if len(input_filename) == 15:
        N = int(input_filename[15])

    else:
        N = int(input_filename[16:18])

    # create an NxN gameboard with a width 1 edge and an RGB color channel
    gameboard = np.zeros((N+2, N+2, 3))
    
    # the inner side of the gameboard should be changed to white
    gameboard[1:N+1, 1:N+1] = [1, 1, 1]

    # loop through the indices and rows of the car positions dataframe
    for i, row in dataframe.iterrows():
        
        # the x and y coordinates correspond to the current column and row respectively
        x = row['col']
        y = row['row']
        
        # find the length of the current car
        length = row['length']
        
        # create random color values
        # the red value is limited to prevent red cars from appearing
        r = random.uniform(0,0.7)
        
        # cars with different lengths are given a slightly different color
        if length == 2:
            g = random.uniform(0,0.8)
            b = random.random()

        else:
            g = random.random()
            b = random.uniform(0,0.8)

        # check if the car is not the red car
        if row['car'] != 'X':
            
            # find the orientation of the car
            if row['orientation'] == 'H':
                
                # add the length to the x coordinate if the orientation is horizontal
                gameboard[y, x:x+length] = [r, g, b]
            else:
                
                # add the length to the y coordinate if the orientation is vertical
                gameboard[y:y+length, x] = [r, g, b]
                
        # car 'X' corresponds to the red car
        else:
            
            # make this car red
            gameboard[y, x:x+length] = [1, 0, 0]
            
            # change the edge block in the exit to white
            gameboard[y, N+1] = [1, 1, 1]

    return gameboard

parser = argparse.ArgumentParser()

# Adding arguments
parser.add_argument("input", help = "input file (csv)")

# Read arguments from command line
args = parser.parse_args()

# Run main with provide arguments
puzzle = gameboard(args.input)

plt.imshow(puzzle)
plt.show()

class game_board():

    def __init__(self, N):
        N = 6
        # create an NxN gameboard with a width 1 edge and an RGB color channel
        self.gameboard = np.zeros((N+2, N+2, 3))

        # the inner side of the gameboard should be changed to white
        self.gameboard[1:N+1, 1:N+1] = [1, 1, 1]

class vehicle():

    # here the cars are made and given a place and an orientation, column is x and row is y
    def __init__(self, car, orientation, col, row, length):
        self.car = car
        self.orientation = orientation
        self.x_pos = col
        self.y_pos = row
        self.length = length
        if car != "X":
            self.color = [random.random, random.random, random.random]
        else: 
            self.color = [1,0,0]

    # here a new position is given to a specific car
    def mover(self):

        # check if the orientation is horizontal or vertiacal because this decides if the cars moves up/down or left/right
        if self.orientation == "H":

            # we have to check if it is at the edge of the board or it is against a different car it should not move in that
            # direction so the car have to be skipped or moved in the different direction on its oritentation.

            # TO DO
            # make a way to check if the surrounding positions of the car has values higher than [0, 0, 0].
            # if the position has a value of [0, 0, 0] the car can move in that direction.
            # KEEP IN MIND that a car covers multiple positons on the board

            # also remind the previous states to prevent a loop on moving a car up and then down etc

            # define the area where the car is on the board 
            self.area_vehicle = [[self.y_pos, self.x_pos], [self.y_pos, self.x_pos + 1]]

            # position infront or behind the car where the car is moved to
            check_spot = [self.y_pos, self.x_pos + self.length + 1]

            # to move the car 
            if game_board[check_spot] == [1,1,1]:
                self.x_pos += 1
                self.area_vehicle = [[self.y_pos, self.x_pos], [self.y_pos, self.x_pos + 1]]

