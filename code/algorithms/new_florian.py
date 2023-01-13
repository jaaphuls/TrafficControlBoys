import pandas as pd
import argparse
import random
import matplotlib.pyplot as plt
import numpy as np

class gameboard():

    def __init__(self, input_filename):
        """
        Arguments: csv input filename with car positions
        
        Creates an NxN gameboard with a black edge and colored cars

        Returns the Rush Hour gameboard
        """
        
        # read the csv input file as a pandas dataframe
        self.dataframe = pd.read_csv(input_filename)

        # find the width and height N of the gameboard
        # the slicing is corrected for N > 9
        if len(input_filename) == 15:
            self.N = int(input_filename[15])

        else:
            self.N = int(input_filename[13])

        # create an NxN gameboard with a width 1 edge and an RGB color channel
        self.gameboard = np.zeros((self.N+2, self.N+2, 3))
        
        # the inner side of the gameboard should be changed to white
        self.gameboard[1:self.N+1, 1:self.N+1] = [1, 1, 1]

    def game_board(self):

        # loop through the indices and rows of the car positions dataframe
        for i, row in self.dataframe.iterrows():
            
            # the x and y coordinates correspond to the current column and row respectively
            self.x = row['col']
            self.y = row['row']
            
            # find the length of the current car
            self.length = row['length']
            
            # create random color values
            # the red value is limited to prevent red cars from appearing
            r = random.uniform(0,0.7)
            
            # cars with different lengths are given a slightly different color
            if self.length == 2:
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
                    self.gameboard[self.y, self.x:self.x+self.length] = [r, g, b]
                else:
                    
                    # add the length to the y coordinate if the orientation is vertical
                    self.gameboard[self.y:self.y+self.length, self.x] = [r, g, b]
                    
            # car 'X' corresponds to the red car
            else:
                
                # make this car red
                self.gameboard[self.y, self.x:self.x+self.length] = [1, 0, 0]
                
                # change the edge block in the exit to white
                self.gameboard[self.y, self.N+1] = [1, 1, 1]

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
            if self.gameboard[check_spot] == [1,1,1]:
                self.x_pos += 1
                self.area_vehicle = [[self.y_pos, self.x_pos], [self.y_pos, self.x_pos + 1]]

'''
parser = argparse.ArgumentParser()

# Adding arguments
parser.add_argument("input", help = "input file (csv)")

# Read arguments from command line
args = parser.parse_args()

# Run main with provide arguments
puzzle = gameboard(args.input)'''

puzzle = gameboard('data/Rushhour6x6_1.csv')

plt.imshow(puzzle)
plt.show()
