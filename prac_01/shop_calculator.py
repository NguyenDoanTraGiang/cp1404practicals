def main():
    num_items = int(input("Number of items: "))
    # number of items validation
    while num_items < 0:
        print("Invalid number of items!")
        num_items = int(input("Number of items: "))
    # get item prices and calculate the total price
    total_price = 0
    for i in range(0, num_items):
        item_price = float(input("Price of item: "))
        total_price = total_price + item_price
    # applying 10% discount if total price is over $100
    if total_price > 100:
        total_price = total_price - total_price * 0.1
    # display final total price
    print("Total price of", num_items, "items is ${:.2f}".format(total_price))


if __name__ == '__main__':
    main()
