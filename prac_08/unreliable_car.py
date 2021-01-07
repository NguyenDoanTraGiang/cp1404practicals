from prac_08.car import Car

class UnreliableCar(Car):
    """Specialised version of Car that include a reliability percentage"""
    def __init__(self, name, fuel, reliability):
        Car.__init__(self, name, fuel)
        self.reliability = reliability
