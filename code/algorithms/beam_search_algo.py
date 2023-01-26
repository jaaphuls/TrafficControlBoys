import random
import time
import queue
from code.classes.vehicle import Vehicle
from code.classes.board import Board

def beam_search(board, board_size, beam_width):
    start_time = time.time()
    previous_states = board.states_list
    previous_states.add(board.string_value)
    
    step = 0

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
        
        for states in current_state.check_move():
            new_game = Board(states, board_size)

            if new_game.string_value not in board.states_list:
                step += 1
                board.states_list.add(new_game.string_value)
                choices_queue.put(new_game)

                if new_game.rush_board[end_coord] == "X":
                    runtime = time.time() - start_time
                    # print(step)
                    return runtime
            else:
                pass
        
        # Implement beam width
        if choices_queue.qsize() > beam_width:
            for i in range(choices_queue.qsize() - beam_width):
                choices_queue.get()
