import random
from code.classes.vehicle import Vehicle
from code.classes.board import Board

# class Random():

#     def __init__(self, board): 
#         self.board = board
#         self.random_step()
        

def random_step(board):

    car = random.choice(board.car_list)
    fifty_fifty = random.random()
    #print(fifty_fifty)
    #print(f' this is car.x: {car.x}')
    #print(f' this is car.y: {car.y}')

    mover = board.check_move(car)

    if mover == 1 and car.orientation == "H":
        car.x += 1

    elif mover == -1 and car.orientation == "H":
        car.x -= 1

    elif mover == 1 and car.orientation == "V":
        car.y -= 1

    elif mover == -1 and car.orientation == "V":
        car.y += 1

    '''
    if car.orientation == 'H': 
        x_left = (car.x - 1)
        x_right = (car.x + car.length)
        print(f'this is left {x_left}')
        print(f'this is right {x_right}')
        
        if x_left >= 1: 
            if self.rush_board[car.y, x_left] == '.' and fifty_fifty < 0.50:
                car.x -= 1
            else:
                print("pass 1 left")
                pass

        if x_right <= self.N - 1: 
            if self.rush_board[car.y, x_right] == '.' and fifty_fifty > 0.50:
                car.x += 1
            else:
                print("pass 1 right")
                pass

        else:
            print("pass2")
            pass

    # car oriention 'V'
    else:
        y_down = (car.y + car.length)
        y_up = (car.y - 1) 
        print(f'this is up {y_up}')
        print(f'this is down {y_down}')

        if y_down <= self.N - 2:
            if self.rush_board[y_down, car.x] == '.' and fifty_fifty > 0.5:  
                car.y += 1
            else:
                print("pass")
                pass

        elif y_up >= 1:
            if self.rush_board[y_up, car.x] == '.' and fifty_fifty < 0.5: 
                car.y -= 1
            else:
                print("pass")
                pass

        else:
            print("pass")
            pass'''

    return board.car_list