import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    # Change to desired directory
    os.chdir('FilesToSort')
    # Print all file in current directory
    print("All file in current directory is {}".format(os.listdir('.')))

    category_to_extension = {}
    mention_category = []  # List to avoid repetition
    for file_name in os.listdir('.'):
        # Ignore directories
        if os.path.isdir(file_name):
            continue
        # Separate file name from file type
        names_and_types = file_name.split('.')

        if names_and_types[1] not in mention_category:
            # Create a dictionary with file extensions as keys
            user_category = input("What category would you like to sort {} files into? ".format(names_and_types[1]))
            # Add file extension into a list to avoid repetition
            mention_category.append(names_and_types[1])
            category_to_extension[names_and_types[1]] = user_category


main()
