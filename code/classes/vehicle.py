
class Vehicle:

    def __init__(self, car, orientation, col, row, length):
        self.color = [0,0,0]
        self.car = car
        self.x = col
        self.y = row
        self.orientation = orientation
        self.length = length 
        self.location_vehicle()

    def location_vehicle(self):

        self.area = []

        for i in range(self.length):

            if self.orientation == "H":
                self.area.append((self.x, self.y))
                self.x += 1
                
            else:
                self.area.append((self.x, self.y))
                self.y += 1
            