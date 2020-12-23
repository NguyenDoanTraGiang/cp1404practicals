from prac_06.guitar import Guitar

print("My guitars!")
guitars = []

# Test code
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

# User input
name = input("Name: ")
while not name == "":
    year = int(input("Year: "))
    cost = float(input("Cost: $"))

    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print("{} added.".format(new_guitar))

# Check if the guitar is vintage or not
print("\n . . . snip . . .")
print("\nThese are my guitars:")
for i, guitar in enumerate(guitars):
    if guitar.is_vintage() is True:
        vintage_string = " (vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>15} ({}), worth ${:10,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                              vintage_string))
