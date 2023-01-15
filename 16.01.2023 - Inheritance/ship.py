from vehicle import Vehicle

class Ship(Vehicle):
    def __init__(self, MMSI_number):
        self.MMSI_number = MMSI_number