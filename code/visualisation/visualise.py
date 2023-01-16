import pandas as pd
import argparse
import random
import matplotlib.pyplot as plt
import numpy as np

def gameboard(car_list, N):
    """
    Arguments: car list with Vehicle objects
    
    Creates an NxN gameboard with a black edge and colored cars

    Returns the Rush Hour gameboard
    """

    # create an NxN gameboard with a width 1 edge and an RGB color channel
    gameboard = np.zeros((N+2, N+2, 3))
    
    # the inner side of the gameboard should be changed to white
    gameboard[1:N+1, 1:N+1] = [1, 1, 1]

    for vehicle_ in car_list:

        for coordinate in (vehicle_.area):

            gameboard[coordinate] = vehicle_.color

      
    plt.imshow(gameboard)
    plt.show()
