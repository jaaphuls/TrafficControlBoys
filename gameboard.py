import pandas as pd

df = pd.read_csv('data/Rushhour6x6_1.csv')

import matplotlib.pyplot as plt
import numpy as np

def gameboard(N, dataframe):
    """
    Arguments: width and height N of the gameboard, dataframe with car positions

    Returns the Rush Hour gameboard
    """

    gameboard = np.zeros((N+2, N+2, 3))
    gameboard[1:N+1, 1:N+1] = gameboard[3,N+1] = 1


    gameboard[3,1:3] = [1,0,0]

    return gameboard

puzzle = gameboard(6, df)
plt.imshow(puzzle)
plt.show()
