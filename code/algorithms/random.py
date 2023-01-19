import random
from code.classes.vehicle import Vehicle
from code.classes.board import Board

class Random():

    def __init__(self, board): 
        self.board = board
        self.random_step()
        

    def random_step(self):

        car = random.choice(self.car_list)
        fifty_fifty = random.random()
        

        if car.orientation == 'H': 
            if car.length == 2: 
                x_left = (car.x - 1)
                x_right = (car.x + 1)
                
                if self.rush_board[car.y, x_left] == '.' and fifty_fifty < 0.5: 
                    newCar = Vehicle(car.car, car.orientation, car.x - 1, car.y, car.length)
                    self.car_list.remove(car) 
                    self.car_list.append(newCar)

                elif self.rush_board[car.y, x_right] == '.' and fifty_fifty > 0.5: 
                    newCar = Vehicle(car.car,car.orientation, car.x + 1, car.y,  car.length)
                    self.car_list.remove(car) 
                    self.car_list.append(newCar)

            elif car.length == 3: 
                x_left = (car.x - 1)
                x_right = (car.x + 2) 

                if self.rush_board[car.y, x_left] == '.' and fifty_fifty > 0.5: 
                    newCar = Vehicle(car.car, car.orientation, car.x - 1, car.y, car.length)
                    self.car_list.remove(car) 
                    self.car_list.append(newCar)
                
                elif self.rush_board[car.y, x_right] == '.' and fifty_fifty < 0.5: 
                    newCar = Vehicle(car.car,car.orientation, car.x + 1, car.y,  car.length)
                    self.car_list.remove(car) 
                    self.car_list.append(newCar)



        # car oriention 'V'
        else:
            if car.length == 2: 
                y_down = (car.y - 1)
                y_up = (car.y + 1) 

                if self.rush_board[y_down, car.x] == '.' and fifty_fifty > 0.,5: 
                    newCar = Vehicle(car.car, car.orientation, car.x, car.y - 1, car.length)
                    self.car_list.remove(car) 
                    self.car_list.append(newCar)

                elif self.rush_board[y_up, car.x] == '.' and fifty_fifty < 0.5: 
                    newCar = Vehicle(car.car,car.orientation, car.x, car.y + 1,  car.length)
                    self.car_list.remove(car) 
                    self.car_list.append(newCar)


            elif car.length == 3: 
                y_down = (car.y - 1)
                y_up = (car.y + 3) 

                if self.rush_board[y_down, car.x] == '.' and fifty_fifty > 0.5: 
                    newCar = Vehicle(car.car, car.orientation, car.x, car.y - 1, car.length)
                    self.car_list.remove(car) 
                    self.car_list.append(newCar)

                elif self.rush_board[y_up, car.x] == '.' and fifty_fifty < 0.5: 
                    newCar = Vehicle(car.car,car.orientation, car.x, car.y + 1,  car.length)
                    self.car_list.remove(car) 
                    self.car_list.append(newCar)

    return self.car_list