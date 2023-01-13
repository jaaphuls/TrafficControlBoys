class vehicle:

    def __init__(self, car, orientation, col, row, length):
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
                temp_x = self.x
                temp_y = self.y
                self.area.append((temp_x, temp_y)) 
                temp_x += 1
            
            if self.orientation == "V":
                temp_x = self.x
                temp_y = self.y
                self.area.append((temp_x, temp_y)) 
                temp_y += 1