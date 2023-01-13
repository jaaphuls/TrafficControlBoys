
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# df = pd.read_csv('data/Rushhour6x6_1.csv')
# df = pd.read_csv('data/Rushhour6x6_2.csv')
# df = pd.read_csv('data/Rushhour6x6_3.csv')
# df = pd.read_csv('data/Rushhour9x9_4.csv')
# df = pd.read_csv('data/Rushhour9x9_5.csv')
# df = pd.read_csv('data/Rushhour9x9_6.csv')
# df = pd.read_csv('data/Rushhour12x12_7.csv')

class vehicle():

    # here the cars are made and given a place and an orientation, column is x and row is y
    def __init__(self, car, orientation, col, row, length):
        self.car = car
        self.orientation = orientation
        self.x_pos = col
        self.y_pos = row
        self.length = length
        if car != 'X':
            self.color = [random.random, random.random, random.random]
        else: 
            self.color = [1,0,0]

    def board(self, rows, columns):
        gameboard = np.zeros((rows, columns))


    # here a new position is given to a specific car
    def mover(self):

        # check if the orientation is horizontal or vertical because this decides if the cars moves up/down or left/right
        if self.orientation == H and 



        

