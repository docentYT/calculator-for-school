from car import Car
from engine import Engine

class Mustang(Car):
    def __init__(self, color, strip_color):
        self.brand = "Ford"
        self.model_name = "Mustang"
        self.strip_color = strip_color

        self.color = color
        self.engine = Engine(309, 407)