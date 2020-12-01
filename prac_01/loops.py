# loop for printing all odd numbers between 1 and 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# loop for printing 10s from 0 to 100
for j in range(0, 110, 10):
    print(j, end=' ')
print()

# loop for printing out the count down from 20 to 1
for k in range(20, 0, -1):  # step is -1 means countdown
    print(k, end=' ')
print()

# loop for printing out the amount of stars based on user's input
num_stars = int(input("Enter the amount of stars: "))
print("Number of stars:", num_stars)
for star in range(0, num_stars):
    print("*", end='')
print()

# print lines of increasing stars. The number of lines is the user's input
num_lines = int(input("Enter the number of lines: "))
for line in range(1, num_lines + 1):
    print("*" * line)
print()
