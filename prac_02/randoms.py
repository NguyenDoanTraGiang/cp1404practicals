import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
# On line 1, I saw a number between 5 and 20. The smallest number I could have seen is 5, and the largest number is 20

# On line 2, I saw either 3, 5, 7, or 9. Line 2 cannot produces a 4 because the step is 2 from 3 onwards.

# On line 3, I saw decimal number between 2.5 and 5.5. The smallest possible number is 2.5, and the largest is 5.5.

# Produce random number between 1 and 100 inclusive
print(random.randint(1, 100))
