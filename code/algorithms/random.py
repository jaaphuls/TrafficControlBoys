# this script contains the code to run the random algorithm
import random
from code.classes.board import Board  
from code.classes.vehicle import Vehicle


def random_step(board): 

    car = random.choice(board.car_list)

    print(car.car)

    able_to_move = board.check_move(car)

    #print(f'this is able to move "{able_to_move}')

    fifty_fifty = random.randint(1, 2)
    print(f' this is fifty: {fifty_fifty}')

    # check in what orientation the car should move
    if car.orientation == 'H': 

        if able_to_move == (True, True): 
            if fifty_fifty == 1:
                print("move to right 1")
                car.x += 1 
            else: 
                print("move to left 1")
                car.x -= 1

        elif able_to_move == (True, False): 
            print("move to left 2")
            car.x -= 1 
        
        elif able_to_move == (False, True):
            print("move to right 2")
            car.x += 1

        else: 
            pass

    elif car.orientation == 'V': 

        if able_to_move == (True, True): 
            if random.randint(1,3) == 1: 
                car.y += 1
            else: 
                car.y -= 1 

        elif able_to_move == (True, False): 
            car.y += 1 

        elif able_to_move == (False, True): 
            car.y -= 1

        else: 
            pass

    car.location_vehicle()

    

