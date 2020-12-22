from prac_06.guitar import Guitar

gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
print(gibson)
print("Gibson L-5 CES get_age() - Expected 98. Got {}". format(gibson.get_age()))
print("Gibson L-5 CES is_vintage() - Expected True. Got {}".format(gibson.is_vintage()))