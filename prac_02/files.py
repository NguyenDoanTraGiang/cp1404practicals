# Question 1:
name_file = open("name.txt", "w")  # create a .txt and write on it
user_name = input("Enter your name: ")  # get user's input
print(user_name, file=name_file)  # write the input into the .txt file
name_file.close()  # close the .txt file so that it save our progress

# Question 2:
name = open("name.txt", "r")  # open the .txt file, read only
sentence = "Your name is " + name.read()  # create the statement with the file's content
print(sentence)  # print the statement

# Question 3:
number = open("numbers.txt", "r")  # open the text file, read only
first_num = number.readline()  # read the first line
second_num = number.readline()  # read the second line
# add up the first two line
two_line_total = int(first_num) + int(second_num)  # Using int() because readline() returns a string
# print out the sum
print("The sum of the first two line is:", two_line_total)

# Question 4:
total = 0
numbers_file = open("numbers.txt", "r")  # open the text file, read only
for each_line in numbers_file:  # read one line at a time
    # add up all the lines
    total = total + int(each_line)  # Using int() because readline() returns a string
# print out the total of all lines
print("\nThe total of all numbers in the text file is:", total)
