import random

# create CONSTANTS:
MAX_RANGE = 45
MIN_RANGE = 1
NUMBER_EACH_LINE = 6

quick_pick_line = int(input("How many quick picks? "))
for line in range(0, quick_pick_line):
    numbers = []
    for num in range(0, NUMBER_EACH_LINE):
        number = random.randint(1, 45)
        while number in numbers:
            number = random.randint(1, 45)
        numbers.append(number)
    print(numbers)