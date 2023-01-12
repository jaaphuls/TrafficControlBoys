import csv
import pandas as pd
import numpy as np
import random
import matplotlib as plt

# from clases.cars import 

class Graph:

    def __init__(self, source_file):

        self.board = self.load_board(source_file)

    def load_board(self, source_file):
        
        self.df = pd.read_csv(source_file)

        # find the size of the board
        N = self.df.max()

        # create an NxN gameboard with a width 1 edge and an RGB color channel
        gameboard = np.zeros((N+2, N+2, 3))
        
        # the inner side of the gameboard should be changed to white
        gameboard[1:N+1, 1:N+1] = [1, 1, 1]

        return gameboard

    def load_cars(self):

        # loop through the indices and rows of the car positions dataframe
        for i, row in self.df.iterrows():
            
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


source_file = "data/Rushhour6x6_1.csv"

puzzle = Graph(source_file)

plt.imshow(puzzle)
plt.show()