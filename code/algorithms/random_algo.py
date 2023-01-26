import random
import time
from code.classes.vehicle import Vehicle
from code.classes.board import Board
from code.visualisation.visualise import show_board


''' In random_step a random car is selected and moved and therefore create a new state. 
The inputs for the function are, a board that contains the info of what car is where on the board,
 and the board size wich is needed to know when the game is solved for the end position of the red (X) car. 
Also the time and the amound of steps it takes to solve the game is tracked. '''
        
def random_step(board, board_size):
    start_time = time.time()

    # this is the board 
    start_board = board
    step = 0

    if board_size == 6: 
        end_coord = 2,5

    if board_size == 9: 
        end_coord = 4,8
    
    if board_size == 12: 
        end_coord = 5, 11
    
    # the loop needs to continue until the game is solved
    while True:
        board.states_list.add(board.car_list)

        # here all the posible moves are created in a list
        choice = start_board.check_move()

        # here one of the posible moves is randomly selected
        this_choice = random.choice(choice)

        # here the start_board is overwritten
        start_board = Board(this_choice, board_size)

        # this is so visualize the board 
        vis_flo = show_board(this_choice, board_size)
        step += 1
        #start_board.create_state()

        # here the board is created
        start_board.create_board()

        # this is used by the check_move
        start_board.visualize()

        # if this is met, the game is solved
        if start_board.rush_board[end_coord] == "X":
            runtime = time.time() - start_time
            
            return step, runtime



## pas die while true nog aan naar: while start_board.rush_board[end_coord] == "X":