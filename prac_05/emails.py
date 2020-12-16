def main():
    email_to_name = {}
    enter_blank = False
    while not enter_blank:
        email = input("Email: ")

        username = email.split("@")

        name = username[0].split(".")
        complete_name = " ".join(name).title()

        email_to_name[email] = complete_name



if __name__ == '__main__':
    main()
