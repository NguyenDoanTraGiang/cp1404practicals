import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    # Change to desired directory
    os.chdir('FilesToSort')
    # Print all file in current directory
    print("All file in current directory is {}".format(os.listdir('.')))

    extension_to_category = {}
    mention_extension = []  # List to avoid repetition
    for file_name in os.listdir('.'):
        # Ignore directories
        if os.path.isdir(file_name):
            continue
        # Separate file name from file type
        names_and_types = file_name.split('.')

        # Create a dictionary with file extensions as keys
        if names_and_types[1] not in mention_extension:
            user_category = input("What category would you like to sort {} files into? ".format(names_and_types[1]))
            # Add file extension into a list to avoid repetition
            mention_extension.append(names_and_types[1])
            extension_to_category[names_and_types[1]] = user_category

        try:
            # Create subdirectories based on categories
            os.mkdir(extension_to_category[names_and_types[1]])
        except FileExistsError:
            pass

        # Move file based on file extension and chosen categories
        shutil.move(file_name, extension_to_category[names_and_types[1]])


main()
