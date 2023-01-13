import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np

class graph():

    def __init__(self, input_filename):
        self.board = self.create_board(input_filename)

    def create_board(self, input_filename):
        """
        Arguments: csv input filename with car positions
        
        Creates an NxN gameboard with a black edge and colored cars

        Returns the Rush Hour gameboard
        """
        
        # read the csv input file as a pandas dataframe
        self.dataframe = pd.read_csv(input_filename)
        
        # find the size of the board
        self.N = self.dataframe.max()

        # create an NxN gameboard with a width 1 edge and an RGB color channel
        self.gameboard = np.zeros((self.N+2, self.N+2, 3))
        
        # the inner side of the gameboard should be changed to white
        self.gameboard[1:self.N+1, 1:self.N+1] = [1, 1, 1]


    def add_vehicles(self):

        # loop through the indices and rows of the car positions dataframe
        for i, row in self.dataframe.iterrows():
            
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
                    self.board[y, x:x+length] = [r, g, b]
                else:
                    
                    # add the length to the y coordinate if the orientation is vertical
                    self.board[y:y+length, x] = [r, g, b]
                    
            # car 'X' corresponds to the red car
            else:
                
                # make this car red
                self.board[y, x:x+length] = [1, 0, 0]
                
                # change the edge block in the exit to white
                self.board[y, self.N+1] = [1, 1, 1]

        #return self.board


file_name = "Rushhour6x6_1.csv"

    # Run main with provide arguments
puzzle = graph(file_name)

plt.imshow(puzzle)
plt.show()
