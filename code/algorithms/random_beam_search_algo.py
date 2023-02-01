import random
import time
import queue
from code.classes.vehicle import Vehicle
from code.classes.board import Board
from code.visualisation.visualise import show_board
from code.algorithms.backtracking import backtrace, check_50_path

# random beam search first algorithm
def random_beam_search(board, board_size, k):
    """
    Implements the random beam search algorithm to solve the "Rush Hour" puzzle game.
    The function takes in the initial state of the puzzle, the size of the board and the amount of beams (k).
    It returns the runtime, the amount of states visited, the depth and the path to the solution.
    """

    dict_moves = {}
    # dict_moves is a dictionary that stores each board state as a key and its parent state as a value.
    dict_moves[board] = None
    # Initializing the starting board state with None as its parent state.
    future_states = []
    # future_states is a list that stores all the next possible states after the current state.
    start_time = time.time()
    # start_time stores the current time at the start of the program.
    previous_states = set()
    # previous_states is a set that stores all the previously visited states.
    previous_states.add(board.string_value)
    # Adding the starting board state to the set of previously visited states.
    step = 1
    # step is a variable that stores the depth of the search tree.
    states_visited = 0
    # states_visited is a variable that stores the number of states visited during the search.


    # The following if-statements determine the end coordinate of the red car based on the size of the board.     
    if board_size == 6: 
        end_coord = 2,5

    if board_size == 9: 
        end_coord = 4,8
    
    if board_size == 12: 
        end_coord = 5, 11

    
    while True :
        # The while loop continues until a solution is found.

        current_state = choices_queue.get()

        states_list, movements = current_state.check_move()
        # Check for the next possible moves

        random.shuffle(states_list) 
        # shuffle the states for randomness
        states_list = states_list[:k] 
        # select the top k states

        for states in states_list:
            # Loop over the possible states for the next move

            new_game = Board(states, board_size)

            if new_game.string_value not in previous_states:
                # If the state has not been visited before

                dict_moves[new_game] = current_state
                # store the parent and child in the moves dictionary

                states_visited += 1
                previous_states.add(new_game.string_value)
               
                future_states.append(new_game)
        
            if new_game.rush_board[end_coord] == "X":
                # If the rush hour game has been solved

                print("Solution found! ")
                runtime = time.time() - start_time
                
                optimal_moves = backtrace(dict_moves, new_game)
                optimal_moves = optimal_moves[::-1]
                # Backtrack the moves for the moves made in the optimal path

                for move in optimal_moves:

                    show_board(move.car_list, board_size)
                    # Visualise the solution

                the_path = check_50_path(optimal_moves)
                # Generate the output file as a csv for check50
                return runtime, states_visited, step, the_path

        if choices_queue.qsize() == 0:      
            # if the queue is empty, a new depth is reached            
                
            step += 1
            print(f'depth = {step}')

            for state in future_states:
                choices_queue.put(state)
            future_states = []
