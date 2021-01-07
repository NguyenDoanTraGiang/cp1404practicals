from prac_08.taxi import Taxi

new_taxi = Taxi("Prius 1", 100, 1.23)
new_taxi.drive(40)
print("Taxi's detail: {}\nTaxi's current fees: ${}".format(new_taxi, new_taxi.get_fare()))