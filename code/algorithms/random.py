import random
from code.classes.vehicle import Vehicle
from code.classes.board import Board

class Random():

    def __init__(self): 
        random_step()
        

    def random_step(self):
        car = random.choice(self.car_list)

        if car.orientation == 'H': 
            if car.length == 2: 
                x_left = (car.x - 1)
                x_right = (car.x + 2)

                if self.rush_board[car.y, x_left] == '.': 
                    newCar = Vehicle(car.id, car.x - 1, car.y, car.orientation, car.length)
                    car_list.remove(car) 
                    car_list.append(newCar)

                elif self.rush_board[car.y, x_right] == '.': 
                    newCar = Vehicle(car.id, car.x + 1, car.y, car.orientation, car.length)
                    car_list.remove(car) 
                    car_list.append(newCar)

            

#     elif car.length == 3: 
#         x_left = (car.x - 1)
#         x_right = (car.x + 3) 

# # car oriention 'V'
# else:
#     if car.length == 2: 
#         y_down = (car.y - 1)
#         y_up = (car.y + 2) 

#     elif car.length == 3: 
#         y_down = (car.y - 1)
#         y_up = (car.y + 3) 

