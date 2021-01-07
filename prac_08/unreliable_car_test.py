from prac_08.unreliable_car import UnreliableCar

my_car = UnreliableCar("Honda", 100, 100)
driven_distance = my_car.drive(50)
print(my_car)
print("I drove {}km today!".format(driven_distance))