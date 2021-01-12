from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """User choose a taxi and drive it, the system display user's bill until user choose quit"""
    bill_to_date = 0
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive")
    print("q)uit, c)hoose taxi, d)rive")
    user_input = input(">>> ").lower()
    while user_input != "q":
        if user_input == "c":
            # Display the taxis and their details
            print("Taxis available: ")
            for index, taxi in enumerate(taxis):
                print("{} - {}".format(index, taxi))

            # Prompt user to choose a taxi
            chosen_taxi = int(input("Choose taxi: "))
            current_taxi = taxis[chosen_taxi]

            # Display bill to date
            print("Bill to date: {}".format(bill_to_date))

        elif user_input == "d":
            # Prompt the user to enter driven distance
            # Display the cost of the trip
            # Display bill to date
            pass
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
