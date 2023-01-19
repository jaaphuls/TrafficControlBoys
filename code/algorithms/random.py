import random
from code.classes.vehicle import Vehicle
from code.classes.board import Board

class Random():

    def __init__(self, board): 
        self.board = board
        self.random_step()
        

    def random_step(self):

        car = random.choice(self.car_list)
        print(car.car)
        fifty_fifty = random.random()
        print(fifty_fifty)
        print(f' this is car.x: {car.x}')
        print(f' this is car.y: {car.y}')


        if car.orientation == 'H': 
            if car.length == 2: 
                x_left = (car.x - 1)
                x_right = (car.x + 1)
                print(f'this is left {x_left}')
                print(f'this is right {x_right}')
                
                if x_left >= 1: 
                    if self.rush_board[car.y, x_left] == '.' and fifty_fifty < 0.5:
                        newCar = Vehicle(car.car, car.orientation, car.x - 1, car.y, car.length)
                        self.car_list.remove(car) 
                        self.car_list.append(newCar)

                if x_right <= self.N - 2: 
                    if self.rush_board[car.y, x_right] == '.' and fifty_fifty > 0.5:
                        newCar = Vehicle(car.car,car.orientation, car.x + 1, car.y,  car.length)
                        self.car_list.remove(car) 
                        self.car_list.append(newCar)

                else:
                    print("pass")
                    pass

            #elif car.length == 3: 
            else:
                x_left = (car.x - 1)
                x_right = (car.x + 1) 
                print(f'this is left {x_left}')
                print(f'this is right {x_right}')

                if x_left >= 1: 
                    if self.rush_board[car.y, x_left] == '.' and fifty_fifty > 0.5:
                        newCar = Vehicle(car.car, car.orientation, car.x - 1, car.y, car.length)
                        self.car_list.remove(car) 
                        self.car_list.append(newCar)

                if x_right <= self.N - 3: 
                    if self.rush_board[car.y, x_right] == '.' and fifty_fifty < 0.5:
                        newCar = Vehicle(car.car,car.orientation, car.x + 1, car.y,  car.length)
                        self.car_list.remove(car) 
                        self.car_list.append(newCar)

                else:
                    print("pass")
                    
                    pass



        # car oriention 'V'
        else:
            if car.length == 2: 
                y_down = (car.y + 1)
                y_up = (car.y - 1) 
                print(f'this is up {y_up}')
                print(f'this is down {y_down}')

                if y_down <= self.N - 2:
                    if self.rush_board[y_down, car.x] == '.' and fifty_fifty > 0.5:  
                        newCar = Vehicle(car.car, car.orientation, car.x, car.y + 1, car.length)
                        self.car_list.remove(car) 
                        self.car_list.append(newCar)

                if y_up >= 1:
                    if self.rush_board[y_up, car.x] == '.' and fifty_fifty < 0.5: 
                        newCar = Vehicle(car.car,car.orientation, car.x, car.y - 1,  car.length)
                        self.car_list.remove(car) 
                        self.car_list.append(newCar)

                else:
                    print("pass")
                    pass


            #elif car.length == 3: 
            else:
                y_down = (car.y + 1)
                y_up = (car.y - 1) 
                print(f'this is up {y_up}')
                print(f'this is down {y_down}')

                if y_down <= self.N - 3: 
                    if self.rush_board[y_down, car.x] == '.' and fifty_fifty > 0.5:
                        newCar = Vehicle(car.car, car.orientation, car.x, car.y + 1, car.length)
                        self.car_list.remove(car) 
                        self.car_list.append(newCar)

                if y_up >= 1: 
                    if self.rush_board[y_up, car.x] == '.' and fifty_fifty < 0.5:
                        newCar = Vehicle(car.car,car.orientation, car.x, car.y - 1,  car.length)
                        self.car_list.remove(car) 
                        self.car_list.append(newCar)
                
                else:
                    print("pass")
                    pass

        return self.car_list