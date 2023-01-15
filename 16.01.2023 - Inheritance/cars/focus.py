from car import Car
from engine import Engine

class Focus(Car):
    def __init__(self, color):
        self.brand = "Ford"
        self.model_name = "Focus"

        self.color = color
        self.engine = Engine(172, 195)