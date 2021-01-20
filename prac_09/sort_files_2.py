import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    # Change to desired directory
    os.chdir('FilesToSort')
    # Print all file in current directory
    print("All file in current directory is {}".format(os.listdir('.')))

    extension_to_category = {}
    mention_category = []  # List to avoid repetition
    for file_name in os.listdir('.'):
        # Ignore directories
        if os.path.isdir(file_name):
            continue
        # Separate file name from file type
        names_and_types = file_name.split('.')

        # Create a dictionary with file extensions as keys
        user_category = input("What category would you like to sort {} files into? ".format(names_and_types[1]))
        # Add file extension into a list to avoid repetition
        extension_to_category[names_and_types[1]] = user_category
        print(extension_to_category)

        try:
            # Create subdirectories based on categories
            os.mkdir(user_category)
        except FileExistsError:
            pass

        # Move file based on file extension and chosen categories
        shutil.move(file_name, user_category)


main()

