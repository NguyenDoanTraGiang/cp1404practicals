password = input("Enter your password: ")

in_length = False
while not in_length:
    if len(password) < 5:
        print("Minimum password length is 5 characters.")
        password = input("Enter your password: ")
    else:
        in_length = True

for char in password:
    print("*", end='')