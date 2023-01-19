import pandas as pd
import argparse
import random
import matplotlib.pyplot as plt
import numpy as np
import time

def gameboard(car_dict, N):
    """
    Arguments: car list with Vehicle objects
    
    Creates an NxN gameboard with a black edge and colored cars

    Returns the Rush Hour gameboard
    """

    # create an NxN gameboard with a width 1 edge and an RGB color channel
    gameboard = np.zeros((N+2, N+2, 3))
    
    # the inner side of the gameboard should be changed to white
    gameboard[1:N+1, 1:N+1] = [1, 1, 1]
    gameboard[3, N+1] = [1, 1, 1]

    for car in car_dict.values():
        print(car[0])

        for coordinate in car[0]:

            gameboard[coordinate] = car[1]

    plt.imshow(gameboard)
    plt.show()
