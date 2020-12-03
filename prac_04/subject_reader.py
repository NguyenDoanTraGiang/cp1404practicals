"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print_data(data)


def print_data(data):
    for subject_data in data:
        print("{} is taught by {} and has {} students".format(subject_data[0], subject_data[1], subject_data[2]))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    subjects_data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subjects_data.append(parts)
    input_file.close()
    return subjects_data


main()
