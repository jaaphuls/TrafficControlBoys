
from code.classes.vehicle import Vehicle
from code.classes.board import Board
from code.visualisation.visualise import show_board
from code.algorithms.random_algo import random_step
from code.algorithms.backtracking import backtrace
from code.algorithms.breadth_first_algo import breadth_first
from code.algorithms.beam_search_algo import beam_search
from code.algorithms.random_beam_search_algo import random_beam_search
import pandas as pd
import argparse
import random
import matplotlib.pyplot as plt
import numpy as np
import time
from tqdm import tqdm
from statistics import mean
import csv

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

    game_number = int(input('Which game would you like to play? \nEnter game number: '))

    algorithm = input('Which algorithm would you like to use? \n1. random \n2. breadth first search \n3. beam search \n')
        
    csv_rh = (f'data/Rushhour{board_size}x{board_size}_{game_number}.csv')

    # read the csv input file as a pandas dataframe
    dataframe = pd.read_csv(csv_rh)

    # loop through the indices and rows of the car positions dataframe
    car_list = []

    for i, row in dataframe.iterrows():
        car_list.append(Vehicle(row['car'], row['orientation'], row['col'], row['row'], row['length']))


    if (algorithm == '1' or algorithm.lower() == 'random'): 
        print("Calculating ... ... ")
        # Run main with provide arguments
        board = Board(car_list, board_size)
        board.create_state()
        board.create_board()
        board.visualize()
        step, runtime, the_path = random_step(board, board_size)
        print('\n ------------------------------------------ \n ')
        print(f'Game number: {game_number}, algorithm: random')
        print(f"The runtime was: {runtime} seconds")
        print(f"The amount of steps taken is: {step}")
        print(f"The path of movements is: {the_path}")
        print('\n ------------------------------------------ \n ')
        file_name = f"code/results/{board_size}x{board_size}_{game_number}_random.csv"

        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["car", "move"])
            for item in the_path:
                writer.writerow(item)


    if (algorithm == '2' or algorithm.lower() == 'breadth first search'): 
        print("Calculating ... ... ")
        # Run main with provide arguments
        board = Board(car_list, board_size)
        board.create_state()
        board.create_board()
        board.visualize()
        runtime, states_visited, step, the_path = breadth_first(board, board_size)
        print('\n ------------------------------------------ \n ')
        print(f'Game number: {game_number}, algorithm: breadth first search')
        print(f"the runtime was: {runtime} seconds")
        print(f"the amount of states visited is: {states_visited}")
        print(f"the amount of steps made: {step}")
        print(f"The path of movements is: {the_path}")
        print('\n ------------------------------------------ \n ')
        file_name = f"code/results/{board_size}x{board_size}_{game_number}_breadth_first.csv"

        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["car", "move"])
            for item in the_path:
                writer.writerow(item)

    if (algorithm == '3' or algorithm.lower() == 'random beam search'): 
        print("Calculating ... ... ")
        board = Board(car_list, board_size)
        board.create_state()
        board.create_board()
        board.visualize()
        runtime, states_visited, step, the_path = random_beam_search(board, board_size, 3)
        print('\n ------------------------------------------ \n ')
        print(f'Game number: {game_number}, algorithm: beam  search')
        print(f"the runtime was: {runtime} seconds")
        print(f"the amount of states visited is: {states_visited}")
        print(f"the amount of steps made: {step}")
        print(f"The path of movements is: {the_path}")
        print('\n ------------------------------------------ \n ')
        file_name = f"code/results/{board_size}x{board_size}_{game_number}_random_beam_search.csv"

        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["car", "move"])
            for item in the_path:
                writer.writerow(item)

        lines = ['\n ------------------------------------------ \n ', f'Game number: {game_number}, algorithm: beam  search', f"the runtime was: {runtime} seconds", 
                f"the amount of states visited is: {states_visited}", f"the amount of steps made: {step}", f"The path of movements is: {the_path}", 
                '\n ------------------------------------------ \n ']
        with open(f'{game_number}_terminal_output_random_beam_search.txt', 'w') as f:
            for line in lines:
                f.write(line)
                f.write('\n')







##### extra code for running the random algorithm 1000 times #####

        # runtimes = []
        # count_list = []

        # for i in tqdm(range(1000)): 

        #     # Run main with provide arguments
        #     board = Board(car_list, board_size)
        #     board.create_state()
        #     board.create_board()
        #     board.visualize()
        #     step, runtime = random_step(board, board_size)
        #     count_list.append(step)
        #     runtimes.append(runtime)

        # plt.figure(figsize=[10,6])
        # plt.hist(runtimes, bins = 30, label= f"mean runtime = {round(mean(runtimes), 5)} seconds \nleast amount of runtime is {round(min(runtimes), 5)} seconds \nmost amount of runtime is {round(max(runtimes), 5)} seconds")
        # plt.xlabel('time (in seconds)')
        # plt.ylabel('number of games')
        # plt.title('1000 games simulated')
        # plt.legend()
        # plt.savefig(f'code/results/random_results/random_algorithm/2_step/results_runtime_game_{game_number}_2_steps')

        # plt.figure(figsize=[10,6])
        # plt.hist(count_list, bins = 30, label = f"mean steps = {mean(count_list)} steps \nleast amount of steps is {min(count_list)} steps \nmost amount of steps is {max(count_list)} steps")
        # plt.xlabel('amount of steps')
        # plt.ylabel('number of games')
        # plt.title('1000 games simulated')
        # plt.legend()
        # plt.savefig(f'code/results/random_results/random_algorithm/2_step/results_steps_game_{game_number}_2_steps')