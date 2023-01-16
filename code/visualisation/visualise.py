import pandas as pd
import argparse
import random
import matplotlib.pyplot as plt
import numpy as np

def gameboard(input_filename, N):
    """
    Arguments: csv input filename with car positions
    
    Creates an NxN gameboard with a black edge and colored cars

    Returns the Rush Hour gameboard
    """

    # create an NxN gameboard with a width 1 edge and an RGB color channel
    gameboard = np.zeros((N+2, N+2, 3))
    
    # the inner side of the gameboard should be changed to white
    gameboard[1:N+1, 1:N+1] = [1, 1, 1]

    for vehicle_ in input_filename:

        print(vehicle_.car)

'''
    # loop through the indices and rows of the car positions dataframe
    for  in input_filename.iterrows():
        
        # the x and y coordinates correspond to the current column and row respectively
        x = row['col']
        y = row['row']
        
        # find the length of the current car
        length = row['length']
        
        # create random color values
        # the red value is limited to prevent red cars from appearing
        # r = random.uniform(0,0.7)
        
        # # cars with different lengths are given a slightly different color
        # if length == 2:
        #     g = random.uniform(0,0.8)
        #     b = random.random()

        # else:
        #     g = random.random()
        #     b = random.uniform(0,0.8)

        # check if the car is not the red car

        if row['car'] != 'X':
            
            # find the orientation of the car
            if row['orientation'] == 'H':
                
                # add the length to the x coordinate if the orientation is horizontal
                gameboard[y, x:x+length] = np.random.choice(range(255),3)/3
            else:
                
                # add the length to the y coordinate if the orientation is vertical
                gameboard[y:y+length, x] = np.random.choice(range(255),3)/3
                
        # car 'X' corresponds to the red car
        else:
            
            # make this car red
            gameboard[y, x:x+length] = [1, 0, 0]
            
            # change the edge block in the exit to white
            gameboard[y, N+1] = [1, 1, 1]


    plt.imshow(gameboard)
    plt.show()
    '''