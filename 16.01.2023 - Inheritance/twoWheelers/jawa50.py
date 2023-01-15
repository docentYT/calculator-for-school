from motocycle import Motocycle
from engine import Engine

class Jawa500(Motocycle):
    def __init__(self, color):
        self.brand = "Jawa"
        self.model_name = "50"

        self.color = color
        self.engine = Engine(2, 3.5)