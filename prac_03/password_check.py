def main():
    password = get_password()

    display_asterisks(password)


def display_asterisks(password):
    for character in password:
        print("*", end='')


def get_password():
    password = input("Enter your password: ")
    in_length = False
    while not in_length:
        if len(password) < 5:
            print("Minimum password length is 5 characters.")
            password = input("Enter your password: ")
        else:
            in_length = True
    return password


if __name__ == '__main__':
    main()
