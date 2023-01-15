from motocycle import Motocycle
from engine import Engine

class Komar(Motocycle):
    def __init__(self, color):
        self.brand = "Romet"
        self.model_name = "Komar"

        self.color = color
        self.engine = Engine(1.4, 2.8)