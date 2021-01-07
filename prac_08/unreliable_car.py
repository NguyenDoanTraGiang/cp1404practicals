from prac_08.car import Car
from random import randint

class UnreliableCar(Car):
    """Specialised version of Car that include a reliability percentage"""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability
