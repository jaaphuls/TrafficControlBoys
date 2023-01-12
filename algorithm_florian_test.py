import pandas as pd
import random 
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data/Rushhour6x6_1.csv')
# df = pd.read_csv('data/Rushhour6x6_2.csv')
# df = pd.read_csv('data/Rushhour6x6_3.csv')
# df = pd.read_csv('data/Rushhour9x9_4.csv')
# df = pd.read_csv('data/Rushhour9x9_5.csv')
# df = pd.read_csv('data/Rushhour9x9_6.csv')
# df = pd.read_csv('data/Rushhour12x12_7.csv')


def gameboard(N, dataframe):
    """
    Arguments: width and height N of the gameboard, dataframe with car positions

    Creates an NxN gameboard with a black edge and colored cars

    Returns the Rush Hour gameboard
    """

    # list with random colors
    color_list = [[0, 0, 0.5], [0, 0, 1], [0, 0.5, 0], \
    [0, 0.5, 0.5], [0, 0.5, 1], [0, 1, 0], [0, 1, 0.5], \
    [0, 1, 1], [0.5, 0, 0], [0.5, 0, 0.5], [0.5, 0, 1], \
    [0.5, 0.5, 0], [0.5, 0.5, 0.5], [0.5, 0.5, 1], \
    [0.5, 1, 0], [0.5, 1, 0.75], [0.5, 1, 1], [1, 0, 0.5], \
    [1, 0, 1], [1, 0.5, 0], [1, 0.5, 0.5], [1, 0.5, 1], \
    [1, 1, 0], [1, 1, 0.5], [0.7, 0.7, 0.7]]

    # create an NxN gameboard with a width 1 edge and an RGB color channel
    gameboard = np.zeros((N+2, N+2, 3))

    # the inner side of the gameboard should be changed to white
    gameboard[1:N+1, 1:N+1] = [1, 1, 1]

    # loop through the indices and rows of the car positions dataframe
    for i, row in dataframe.iterrows():

        # reset to 0 if i reaches the length of the color list
        if i >= len(color_list):
            i -= len(color_list)

        # the x and y coordinates correspond to the current column and row respectively
        x = row['col']
        y = row['row']

        # find the length of the current car
        length = row['length']

        # check if the car is not the red car
        if row['car'] != 'X':

            # find the orientation of the car
            if row['orientation'] == 'H':

                # add the length to the x coordinate if the orientation is horizontal
                gameboard[y, x:x+length] = color_list[i]
            else:

                # add the length to the y coordinate if the orientation is vertical
                gameboard[y:y+length, x] = color_list[i]

        # car 'X' corresponds to the red car
        else:

            # make this car red
            gameboard[y, x:x+length] = [1, 0, 0]

            # change the edge block in the exit to white
            gameboard[y, N+1] = [1, 1, 1]

    return gameboard

puzzle = gameboard(6, df)
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

