# Question 1:
numbers = []
for num in range(0, 5):
    number = int(input("Number: "))
    numbers.append(number)
print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the number is", sum(numbers) / len(numbers))

# Question 2:
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
name_input = input("\nEnter your name: ")
if name_input in usernames:
    print("Access granted")
else:
    print("Access denied")
