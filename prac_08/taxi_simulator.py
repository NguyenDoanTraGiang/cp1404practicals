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
            display_taxis(taxis)
            # Prompt user to choose a taxi
            chosen_taxi = int(input("Choose taxi: "))
            current_taxi = taxis[chosen_taxi]
            # Display bill to date
            print("Bill to date: ${:.2f}".format(bill_to_date))

        elif user_input == "d":
            # User cannot proceed if no taxi is chosen
            if current_taxi is None:
                print("You haven't choose a taxi yet!")
            # Prompt the user to enter driven distance
            current_taxi.start_fare()
            distance = float(input("Drive how far? "))
            current_taxi.drive(distance)
            # Display the cost of the trip
            current_cost = current_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_cost))
            # Display bill to date
            bill_to_date += current_cost
            print("Bill to date: ${:.2f}".format(bill_to_date))
        else:
            print("Invalid choice")

        # Prompt the user to choose the menu again
        print("q)uit, c)hoose taxi, d)rive")
        user_input = input(">>> ").lower()

    # Display when user choose quit
    print("Total trip cost: ${:.2f}".format(bill_to_date))
    print("Taxi are now: ")
    display_taxis(taxis)


def display_taxis(taxis):
    for index, taxi in enumerate(taxis):
        print("{} - {}".format(index, taxi))


if __name__ == "__main__":
    main()
