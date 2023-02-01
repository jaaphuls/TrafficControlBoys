
from code.classes.vehicle import Vehicle
from code.classes.board import Board
from code.visualisation.visualise import show_board
from code.algorithms.random_algo import random_step
from code.algorithms.backtracking import backtrace
from code.algorithms.breadth_first_algo import breadth_first
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
        
        # this dictionary allows the user to give two different input notations for the board size
        dimensions = {'6x6' : '6', '9x9' : '9', '12x12' : '12'}
        
        board_size = input("What are the board dimensions (6x6, 9x9 or 12x12)? \n")
        
        # the input should first be used as a key in the dimensions dictionary if the NxN notation was used
        if board_size in dimensions:
            board_size = int(dimensions[board_size])
        
        # the input can be directly converted into an integer if the N notation was used
        elif board_size in dimensions.values():
            board_size = int(board_size)

        else:
            print("There are no boards with these dimensions, please choose the correct dimensions!")

    # the user is asked which game should be played with which algorithm
    game_number = int(input('Which game would you like to play? \nEnter game number: '))
    algorithm = input('Which algorithm would you like to use? \n1. random \n2. breadth first search \n3. beam search \n')
    
    # here the input is converted into a file name to load the csv from the data directory
    csv_rh = (f'data/Rushhour{board_size}x{board_size}_{game_number}.csv')

    # read the csv input file as a pandas dataframe
    dataframe = pd.read_csv(csv_rh)

    # this will be the original list of cars on the starting positions
    car_list = []
    
    # loop through the indices and rows of the car positions dataframe
    for i, row in dataframe.iterrows():
        
        # create Vehicle objects with data from the csv file and put them in car_list
        car_list.append(Vehicle(row['car'], row['orientation'], row['col'], row['row'], row['length']))


    # ------------------------------------- random algorithm -------------------------------------      


    if (algorithm == '1' or algorithm.lower() == 'random'): 
        print("Calculating ... ... ")

        # create the Board object with the initial car list
        board = Board(car_list, board_size)

        # run the random algorithm until a solution is found
        step, runtime, the_path = random_step(board, board_size)

        # give the user some information about the run
        print('\n ------------------------------------------ \n ')
        print(f'Game number: {game_number}, algorithm: random')
        print(f"The runtime was: {runtime} seconds")
        print(f"The amount of steps taken is: {step}")
        print(f"The path of movements is: {the_path}")
        print('\n ------------------------------------------ \n ')

        # create the output file name for the random algorithm
        file_name = f"{board_size}x{board_size}_{game_number}_random.csv"

        # create a new csv output file
        with open(f'code/results/random_results/{file_name}', "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["car", "move"])
            for item in the_path:
                writer.writerow(item)

        # create lines with information about the run
        lines = ['\n ------------------------------------------ \n ', 
                f'Game number: {game_number}, algorithm: random', 
                f"the runtime was: {runtime} seconds", 
                f"The amount of steps taken is: {step}", 
                f"The path of movements is: {the_path}", 
                '\n ------------------------------------------ \n ']

        # write the lines in the output file   
        with open(f'code/results/random_results/{board_size}x{board_size}_{game_number}terminal_output_random.txt', 'w') as f:
            for line in lines:
                f.write(line)
                f.write('\n')


    # ------------------------------------- breadth first search algorithm -------------------------------------      



    if (algorithm == '2' or algorithm.lower() == 'breadth first search'): 
        print("Calculating ... ... ")

        # create the Board object with the initial car list
        board = Board(car_list, board_size)

        # run the breadth first search algorithm until a solution is found
        runtime, states_visited, step, the_path = breadth_first(board, board_size)

        # give the user some information about the run
        print('\n ------------------------------------------ \n ')
        print(f'Game number: {game_number}, algorithm: breadth first search')
        print(f"the runtime was: {runtime} seconds")
        print(f"the amount of states visited is: {states_visited}")
        print(f"the amount of steps made: {step}")
        print(f"The path of movements is: {the_path}")
        print('\n ------------------------------------------ \n ')

        # create the output file name for the breadth first search algorithm
        file_name = f"{board_size}x{board_size}_{game_number}_bfs.csv"

        # create a new csv output file
        with open(f'code/results/breadth_first_search/{file_name}', "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["car", "move"])
            for item in the_path:
                writer.writerow(item)

        # create lines with information about the run
        lines = ['\n ------------------------------------------ \n ',
                f'Game number: {game_number}, algorithm: breadth first search',
                f"the runtime was: {runtime} seconds", 
                f"the amount of states visited is: {states_visited}", 
                f"the amount of steps made: {step}", 
                f"The path of movements is: {the_path}", 
                '\n ------------------------------------------ \n ']

        # write the lines in the output file  
        with open(f'code/results/breadth_first_search/{board_size}x{board_size}_{game_number}_terminal_output_bfs.txt', 'w') as f:
            for line in lines:
                f.write(line)
                f.write('\n')


        # ------------------------------------- random beam search algorithm -------------------------------------      


    if (algorithm == '3' or algorithm.lower() == 'random beam search'): 
        print("Calculating ... ... ")

        # create the Board object with the initial car list
        board = Board(car_list, board_size)

        # run the random beam search algorithm with k = 3 until a solution is found
        runtime, states_visited, step, the_path = random_beam_search(board, board_size, 3)

        # give the user some information about the run
        print('\n ------------------------------------------ \n ')
        print(f'Game number: {game_number}, algorithm: beam  search')
        print(f"the runtime was: {runtime} seconds")
        print(f"the amount of states visited is: {states_visited}")
        print(f"the amount of steps made: {step}")
        print(f"The path of movements is: {the_path}")
        print('\n ------------------------------------------ \n ')

        # create the output file name for the random beam search algorithm
        file_name = f"{board_size}x{board_size}_{game_number}_rbs.csv"

        # create a new csv output file
        with open(f'code/results/random_beam_search/{file_name}', "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["car", "move"])
            for item in the_path:
                writer.writerow(item)

        # create lines with information about the run
        lines = ['\n ------------------------------------------ \n ', 
                f'Game number: {game_number}, algorithm: beam  search', 
                f"the runtime was: {runtime} seconds", 
                f"the amount of states visited is: {states_visited}", 
                f"the amount of steps made: {step}", 
                f"The path of movements is: {the_path}", 
                '\n ------------------------------------------ \n ']

        # write the lines in the output file              
        with open(f'code/results/random_beam_search/{board_size}x{board_size}_{game_number}_terminal_output_rbs.txt', 'w') as f:
            for line in lines:
                f.write(line)
                f.write('\n')

