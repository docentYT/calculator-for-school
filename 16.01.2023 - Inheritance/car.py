from twoTrack import TwoTrack

class Car(TwoTrack):
    def __init__(self, vin_number, number_of_doors, color):
        self.vin_number = vin_number
        self.number_of_doors = number_of_doors
        self.color = color