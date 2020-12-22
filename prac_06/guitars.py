from prac_06.guitar import Guitar
print("My guitars!")
guitars = []
enter_blank_name = False

while not enter_blank_name:
    name = input("Name: ")

    if name == "":
        break

    year = int(input("Year: "))
    cost = int(input("Cost: "))

