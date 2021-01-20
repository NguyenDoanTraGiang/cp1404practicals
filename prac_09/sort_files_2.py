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


main()
