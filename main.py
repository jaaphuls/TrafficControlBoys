
from code.classes.vehicle import Vehicle
from code.classes.board import Board
from code.visualisation.visualise import gameboard
import pandas as pd
import argparse
import random
import matplotlib.pyplot as plt
import numpy as np
from code.algorithms.random_algo import random_step
import time
from tqdm import tqdm
from statistics import mean

if __name__ == '__main__':
    
    # this code block asks for a user input and keeps asking until a good input is given
    board_size = None

    while type(board_size) != int:
        dimensions = {'6x6' : '6', '9x9' : '9', '12x12' : '12'}
        
        board_size = input("What are the board dimensions (6x6, 9x9 or 12x12)? \n")
        
        if board_size in dimensions:
            board_size = int(dimensions[board_size])
        
        elif board_size in dimensions.values():
            board_size = int(board_size)

        else:
            print("There are no boards with these dimensions, please choose the correct dimensions!")

    game_number = int(input('Which game would you like to play? \n Enter game number \n'))
        
    csv_rh = (f'data/Rushhour{board_size}x{board_size}_{game_number}.csv')

    # read the csv input file as a pandas dataframe
    dataframe = pd.read_csv(csv_rh)

    # loop through the indices and rows of the car positions dataframe
    car_list = []

    for i, row in dataframe.iterrows():
        car_list.append(Vehicle(row['car'], row['orientation'], row['col'], row['row'], row['length']))


    runtimes = []
    count_list = []

    for i in tqdm(range(1000)): 

        # Run main with provide arguments
        board = Board(car_list, board_size)
        board.create_state()
        board.create_board()
        board.visualize()
        new_car_list = random_step(board, board_size)

        count_list.append(new_car_list[0])
        runtimes.append(new_car_list[1])

    plt.figure(figsize=[10,6])
    plt.hist(runtimes, bins = 30, label= f"mean runtime = {round(mean(runtimes), 5)} seconds \nleast amount of runtime is {round(min(runtimes), 5)} seconds \nmost amount of runtime is {round(max(runtimes), 5)} seconds")
    plt.xlabel('time (in seconds)')
    plt.ylabel('number of games')
    plt.title('1000 games simulated')
    plt.legend()
    plt.savefig(f'code/results/random_results/2_step/results_runtime_game_{game_number}_2_steps')

    plt.figure(figsize=[10,6])
    plt.hist(count_list, bins = 30, label = f"mean steps = {mean(count_list)} steps \nleast amount of steps is {min(count_list)} steps \nmost amount of steps is {max(count_list)} steps")
    plt.xlabel('amount of steps')
    plt.ylabel('number of games')
    plt.title('1000 games simulated')
    plt.legend()
    plt.savefig(f'code/results/random_results/2_step/results_steps_game_{game_number}_2_steps')



    

