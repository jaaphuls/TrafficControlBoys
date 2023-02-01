import random
import time
import queue
from code.classes.vehicle import Vehicle
from code.classes.board import Board

def beam_search(board, board_size, beam_width):
      """
    Implements the Beam Search algorithm to solve the "Rush Hour" puzzle game.
    The function takes in the initial state of the puzzle, the size of the board, and the beam width.
    It returns the runtime, which is the time elapsed since the start of the search.
    """
    step = 0

    #record the start time of the search
    start_time = time.time()

    #get the list of previously seen states
    previous_states = board.states_list

    # add the current state to the list of seen states
    previous_states.add(board.string_value)
    
    
    #initialize a queue to store the possible next states of the puzzle
    choices_queue = queue.Queue()
    choices_queue.put(board)

    #set the end coordinate of the puzzle based on the board size
    if board_size == 6: 
        end_coord = 2,5
    elif board_size == 9: 
        end_coord = 4,8
    elif board_size == 12: 
        end_coord = 5, 11

    #keep generating possible next states until a solution is found
    while True:

        #get the current state from the queue
        current_state = choices_queue.get()

        #generate all possible new states from the current state
        for states in current_state.check_move():
            new_game = Board(states, board_size)

            #check if the new state has already been seen
            if new_game.string_value not in board.states_list:
                step += 1

                #add the new state to the list of seen states and queue
                board.states_list.add(new_game.string_value)
                choices_queue.put(new_game)

                # check if the new state is a solution
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
