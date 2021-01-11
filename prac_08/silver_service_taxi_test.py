from prac_08.silver_service_taxi import SilverServiceTaxi

new_silver_service_taxi = SilverServiceTaxi("Hummer", 200, 2)
new_silver_service_taxi.drive(18)

print(new_silver_service_taxi)
print("The fancy taxi's fare is ${:.2f}".format(new_silver_service_taxi.get_fare()))
