import random
import time
import queue
from code.classes.vehicle import Vehicle
from code.classes.board import Board

def breadth_first(board, board_size):
    start_time = time.time()
    start_board = board
    previous_states = []
    choices_queue = queue.Queue()
    
    if board_size == 6: 
        end_coord = 2,5

    if board_size == 9: 
        end_coord = 4,8
    
    if board_size == 12: 
        end_coord = 5, 11


    while True:

        choice = start_board.check_move()
        choices_queue.put(choice)

        while not choices_queue.empty():
            current_state = choices_queue.get()

            if current_state not in previous_states:

                previous_states.append(current_state)

                new_board = Board(current_state, board_size) 
                new_board.create_board()
                new_board.visualize()

                choices_queue.put(new_board)


        
                if new_board.rush_board[end_coord] == "X":
                    runtime = time.time() - start_time
            
                    return runtime

        
