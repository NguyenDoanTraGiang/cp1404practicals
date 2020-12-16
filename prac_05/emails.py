def main():
    email_to_name = {}

    enter_blank = False
    while not enter_blank:
        email = input("Email: ")

        if email == "":
            enter_blank = True
        else:
            for email, name in email_to_name.items():
                print("{} ({})".format(email_to_name[name], email))

        username = email.split("@")

        name = username[0].split(".")
        complete_name = " ".join(name).title()

        email_to_name[email] = complete_name

        confirm_name = input("Is your name {}? (Y/n) ".format(email_to_name[email])).lower()
        if confirm_name == "" or confirm_name in "yes":
            break
        elif confirm_name in "no":
            new_name = input("Name: ").title()
            email_to_name[email] = new_name


if __name__ == '__main__':
    main()
