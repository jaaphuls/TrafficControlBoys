import random
import time
from code.classes.vehicle import Vehicle
from code.classes.board import Board

        
def random_step(board, board_size):
    start_time = time.time()
    start_board = board
    steps = 0
    
    while True:
        choice = start_board.check_move()
        print(choice)
        start_board = Board(random.choice(choice), board_size)
        steps += 1
        start_board.create_state()
        start_board.create_board()
        start_board.visualize()

        if board.rush_board[2, 5] == "X":
            
            print(f'the total steps were {step}')
            print(f"solvetime = {time.time() - start_time} seconds")
            
            return exit()
