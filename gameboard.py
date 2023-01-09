import pandas as pd

df = pd.read_csv('data/Rushhour6x6_1.csv')
# df = pd.read_csv('data/Rushhour6x6_2.csv')
# df = pd.read_csv('data/Rushhour6x6_3.csv')


import matplotlib.pyplot as plt
import numpy as np

print(df)

def gameboard(N, dataframe):
    """
    Arguments: width and height N of the gameboard, dataframe with car positions
    
    Creates an NxN gameboard with an edge

    Returns the Rush Hour gameboard
    """
    
    # list with random colors
    color_list = [[0.5, 0.5, 0], [0, 1, 0], [0, 0.5, 0], [0, 1, 1],\
    [0, 0.5, 0.5], [0, 0, 1], [0, 0, 0.5], [1, 0, 1], \
    [0.5, 0, 0.5], [0.5,0.5,0.5], [1,1,0], [1, 0.5, 0]]

    # create an NxN gameboard with an edge 1 and an RGB color channel
    gameboard = np.zeros((N+2, N+2, 3))
    gameboard[1:N+1, 1:N+1] = gameboard[3,N+1] = 1

    for i, row in dataframe.iterrows():
        x = row['col']
        y = row['row']

        length = row['length']

        if row['car'] != 'X':
            if row['orientation'] == 'H':
                gameboard[y,x:x+length] = color_list[i]

            else:
                gameboard[y:y+length,x] = color_list[i]

        else:
            gameboard[y,x:x+length] = [1,0,0]

    return gameboard

puzzle = gameboard(6, df)
plt.imshow(puzzle)
plt.show()
