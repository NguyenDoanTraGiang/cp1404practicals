def main():
    email_to_name = {}

    email = input("Email: ")

    username = email.split("@")

    name = username[0].split(".")
    complete_name = " ".join(name).title()

if __name__ == '__main__':
    main()
