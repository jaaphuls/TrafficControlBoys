import random
import time
import queue
from code.classes.vehicle import Vehicle
from code.classes.board import Board
from code.visualisation.visualise import show_board
from code.algorithms.backtracking import backtrace, check_50_path


# breadth first algorithm
def breadth_first(board, board_size):
    dict_moves = {}
    dict_moves[board] = None
    future_states = []
    start_time = time.time()
    previous_states = set()
    previous_states.add(board.string_value)
    step = 1
    states_visited = 0

    choices_queue = queue.Queue()
    choices_queue.put(board)

    
    if board_size == 6: 
        end_coord = 2,5

    if board_size == 9: 
        end_coord = 4,8
    
    if board_size == 12: 
        end_coord = 5, 11

    
    while True :
        current_state = choices_queue.get()

        states_list, movements = current_state.check_move()

        for states in states_list:
           
            new_game = Board(states, board_size)

            if new_game.string_value not in previous_states:
                dict_moves[new_game] = current_state

                states_visited += 1
                previous_states.add(new_game.string_value)
               
                future_states.append(new_game)
        
            if new_game.rush_board[end_coord] == "X":
                runtime = time.time() - start_time
                
                optimal_moves = backtrace(dict_moves, new_game)
                optimal_moves = optimal_moves[::-1]

                for move in optimal_moves:

                    show_board(move.car_list, board_size)

                the_path = check_50_path(optimal_moves)

                return runtime, states_visited, step, the_path

        if choices_queue.qsize() == 0:           
                
            step += 1

            for state in future_states:
                choices_queue.put(state)
            future_states = []
