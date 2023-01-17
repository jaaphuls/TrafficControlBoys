# this script contains the code to run the random algorithm
import random
from code.classes.board import Board  
from code.classes.vehicle import Vehicle


def random_step(board): 

    car = random.choice(board.car_list)

    able_to_move = board.check_move(car)

    # check in what orientation the car should move
    if car.orientation == 'H': 

        if able_to_move == (True, True): 
            if random.randint(1, 2) != 1:
                car.x += 1 
            else: 
                car.x -= 1

        elif able_to_move == (True, False): 
            car.x -= 1 
        
        elif able_to_move == (False, True):
            car.x += 1

    elif car.orientation == 'V': 

        if able_to_move == (True, True): 
            if random.randint(1,2) != 1: 
                car.y += 1
            else: 
                car.y -= 1 

        elif able_to_move == (True, False): 
            car.y += 1 

        elif able_to_move == (False, True): 
            car.y -= 1

    car.location_vehicle()

    

