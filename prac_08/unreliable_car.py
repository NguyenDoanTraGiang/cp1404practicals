from prac_08.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of Car that include a reliability percentage"""
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Only drive if a random number < reliability"""
        if randint(0, 100) > self.reliability:
            distance = 0
        # Drive the car regardless of the distance
        driven_distance = super().drive(distance)
        return driven_distance
