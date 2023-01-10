import pandas as pd

# df = pd.read_csv('data/Rushhour6x6_1.csv')
# df = pd.read_csv('data/Rushhour6x6_2.csv')
# df = pd.read_csv('data/Rushhour6x6_3.csv')
# df = pd.read_csv('data/Rushhour9x9_4.csv')
# df = pd.read_csv('data/Rushhour9x9_5.csv')
df = pd.read_csv('data/Rushhour9x9_6.csv')
# df = pd.read_csv('data/Rushhour12x12_7.csv')


import matplotlib.pyplot as plt
import numpy as np

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
    [0.5, 1, 0], [0.5, 1, 0.25], [0.5, 1, 1], [1, 0, 0.5], \
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

puzzle = gameboard(9, df)
plt.imshow(puzzle)
plt.show()
