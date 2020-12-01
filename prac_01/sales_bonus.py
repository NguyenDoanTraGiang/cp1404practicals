"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    sales = float(input("Enter sales: $"))
    while sales >= 0:
        if sales < 1000:
            user_bonus = sales * 0.1
            print("Your bonus is:", user_bonus)
        else:
            user_bonus = sales * 0.15
            print("Your bonus is:", user_bonus)


if __name__ == '__main__':
    main()
