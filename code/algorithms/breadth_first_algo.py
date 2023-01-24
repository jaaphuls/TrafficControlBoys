import random
import time
import queue
from code.classes.vehicle import Vehicle
from code.classes.board import Board

# breadth first algorithm
def breadth_first(board, board_size):
    start_time = time.time()
    start_board = board
    previous_states = set()
    previous_states.update((board.states_list))
    step = 0

    choices_queue = queue.Queue()
    choices_queue.put(board)

    
    if board_size == 6: 
        end_coord = 2,5

    if board_size == 9: 
        end_coord = 4,8
    
    if board_size == 12: 
        end_coord = 5, 11


    while True:
        current_state = choices_queue.get()
        step += 1
        print(step)

        for states in current_state.check_move():

            new_game = Board(states, board_size)
            new_game.create_state()
            

            if new_game.states_list not in previous_states:
                
                print(new_game.states_list)
                print(previous_states)
                previous_states.update((new_game.states_list))
               
                new_game.create_board()
                new_game.visualize()

                choices_queue.put(new_game)

                if new_game.rush_board[end_coord] == "X":
                    runtime = time.time() - start_time
                    print(step)
                    return runtime
            else:
                pass
        
