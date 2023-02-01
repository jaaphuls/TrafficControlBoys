import random
import time
from code.classes.vehicle import Vehicle
from code.classes.board import Board
from code.visualisation.visualise import show_board
from code.algorithms.backtracking import backtrace, check_50_path
# Importing the libraries and functions


def random_step(board, board_size):
    ''' 
    In random_step a random car is selected and moved and therefore create a new state. 
    The inputs for the function are, a board that contains the info of what car is where on the board,
    and the board size wich is needed to know when the game is solved for the end position of the red (X) car. 
    Also the time and the amound of steps it takes to solve the game is tracked. 
    '''

    # start the time and step count
    start_time = time.time()
    step = 0
    movement_list = []

    if board_size == 6: 
        end_coord = 2,5

    if board_size == 9: 
        end_coord = 4,8
    
    if board_size == 12: 
        end_coord = 5,11
    
    # the loop needs to continue until the game is solved
    while board.rush_board[end_coord] != "X":
        # here all the posible moves are created in a list
        choice, movements = board.check_move()

        # here one of the posible moves is randomly selected
        this_choice = random.choice(choice)

        movement_list.append(board)

        # here the board is overwritten
        board = Board(this_choice, board_size)

        step += 1
    
    the_path = check_50_path(movement_list)
    
    runtime = time.time() - start_time
    
    return step, runtime, the_path