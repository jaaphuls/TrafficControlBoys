import random
import time
import queue
from code.classes.vehicle import Vehicle
from code.classes.board import Board
from code.visualisation.visualise import show_board


def random_beam_search(board, board_size, k=3):
    start_time = time.time()
    previous_states = board.states_list
    previous_states.add(board.string_value)
    
    step = 0
    depth = 0

    choices_queue = queue.Queue()
    choices_queue.put(board)

    if board_size == 6: 
        end_coord = 2,5
    elif board_size == 9: 
        end_coord = 4,8
    elif board_size == 12: 
        end_coord = 5, 11

    while True:
        current_state = choices_queue.get()
        next_states = current_state.check_move()
        random.shuffle(next_states) # shuffle the states for randomness
        next_states = next_states[:k] # select the top k states
        for states in next_states:
            new_game = Board(states, board_size)
            if new_game.string_value not in previous_states:
                step += 1
                previous_states.add(new_game.string_value)
                new_game.create_board()
                new_game.visualize()
                choices_queue.put(new_game)
                #vis_flo = show_board(states, board_size)

                if new_game.rush_board[end_coord] == "X":
                    runtime = time.time() - start_time
                    
                    return runtime, step, depth
            else:
                pass
