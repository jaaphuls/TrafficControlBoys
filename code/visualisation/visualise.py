import pandas as pd
import argparse
import random
import matplotlib.pyplot as plt
import numpy as np
import time
from code.classes.vehicle import Vehicle

def show_board(state, N):
    """
    Arguments: car list with Vehicle objects
    
    Creates an NxN gameboard with a black edge and colored cars

    Returns the Rush Hour gameboard
    """

    # create an NxN gameboard with a width 1 edge and an RGB color channel
    gameboard = np.zeros((N+2, N+2, 3))
    
    # the inner side of the gameboard should be changed to white
    gameboard[1:N+1, 1:N+1] = [1, 1, 1]
    #gameboard[3, N+1] = [1, 1, 1]

    for car in state:

        if car.car == "X":
            gameboard[car.y+1, N+1] = [1, 1, 1]

        twer = car.color

        if car.length == 2:
            if car.orientation == "H":

                gameboard[car.y+1, car.x+1] = twer
                gameboard[car.y+1, car.x+2] = twer
                #[twer, twer, twer]
            else:
                gameboard[car.y+1, car.x+1] = twer
                gameboard[car.y+2, car.x+1] = twer
        
        else:
            if car.orientation == "H":

                gameboard[car.y+1, car.x+1] = twer
                gameboard[car.y+1, car.x+2] = twer
                gameboard[car.y+1, car.x+3] = twer

            else:
                gameboard[car.y+1, car.x+1] = twer
                gameboard[car.y+2, car.x+1] = twer
                gameboard[car.y+3, car.x+1] = twer


    plt.imshow(gameboard)
    plt.pause(0.1)
    plt.clf()
  
