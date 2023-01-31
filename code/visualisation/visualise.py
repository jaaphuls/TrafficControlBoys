import pandas as pd
import argparse
import random
import matplotlib.pyplot as plt
import numpy as np
import time
from code.classes.vehicle import Vehicle

'''In this function the board can be visualized with colors.
input: the state wich is a list with the car objects that contain all the cars information, and the size of the board (N).'''

def show_board(state, N):

    # create an NxN gameboard with a width 1 edge and an RGB color channel
    gameboard = np.zeros((N+2, N+2, 3))
    
    # the inner side of the gameboard should be changed to white
    gameboard[1:N+1, 1:N+1] = [1, 1, 1]

    # get every induvidual car of the list
    for car in state:

        # make the square on the right edge in the row of the red car white
        if car.car == "X":
            gameboard[car.y+1, N+1] = [1, 1, 1]

        car_color = car.color

        # change the location of the car on the board to the color of the car
        if car.length == 2:
            if car.orientation == "H":
                gameboard[car.y+1, car.x+1] = car_color
                gameboard[car.y+1, car.x+2] = car_color
                
            else:
                gameboard[car.y+1, car.x+1] = car_color
                gameboard[car.y+2, car.x+1] = car_color
        
        else:
            if car.orientation == "H":
                gameboard[car.y+1, car.x+1] = car_color
                gameboard[car.y+1, car.x+2] = car_color
                gameboard[car.y+1, car.x+3] = car_color

            else:
                gameboard[car.y+1, car.x+1] = car_color
                gameboard[car.y+2, car.x+1] = car_color
                gameboard[car.y+3, car.x+1] = car_color


    # this will show the board and update it every tenth of a second and delete the old "picture"
    plt.imshow(gameboard)
    plt.pause(0.3)
    plt.clf()
  
