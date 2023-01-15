from car import Car
from engine import Engine

class TeslaS(Car):
    def __init__(self, color):
        self.brand = "Tesla"
        self.model_name = "Model S"

        self.color = color
        self.engine = Engine(306, -1)