# this script contains the code to run the random algorithm
import random
import copy
from code.classes.board import Board  
from code.classes.vehicle import Vehicle


def random_step(board): 

    car = random.choice(board.car_list)

    new_car_list = board.car_list.copy()

    able_to_move = board.check_move(car)

    fifty_fifty = random.randint(1, 2)

    # check in what orientation the car should move
    if car.orientation == 'H': 

        if able_to_move == (True, True): 
            if fifty_fifty == 1:
                newCar = Vehicle(car.car, car.orientation, car.x + 1, car.y, car.length)

            else: 
                newCar = Vehicle(car.car, car.orientation, car.x - 1, car.y, car.length)

        elif able_to_move == (True, False): 
            newCar = Vehicle(car.car, car.orientation, car.x - 1, car.y, car.length)
        
        elif able_to_move == (False, True):
            newCar = Vehicle(car.car, car.orientation, car.x + 1, car.y, car.length)

        else: 
            pass

    elif car.orientation == 'V': 

        if able_to_move == (True, True): 
            if fifty_fifty == 1: 
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

    new_car_list.remove(car)
    new_car_list.append(newCar)

    return new_car_list



    

