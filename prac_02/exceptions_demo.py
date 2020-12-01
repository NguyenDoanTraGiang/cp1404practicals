"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    # While loop to validate denominator. User cannot enter 0 for the denominator
    while denominator == 0:
        print("Denominator cannot be 0! Please enter again.")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# 1. When will a ValueError occur?
# The ValueError happens when the user enter decimal numbers or letters

# 2. When will a ZeroDivisionError occur?
# This error happens when the user enter 0 for the denominator input

# 3. Could you change the code to avoid the possibility of a ZeroDivisionError?
# Putting a while loop that will not break until the user enter a valid denominator
# Changes to the code has been made
