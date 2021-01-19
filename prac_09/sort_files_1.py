import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    # Change to desired directory
    os.chdir('FilesToSort')
    # Print all file in current directory
    print("All file in current directory is {}".format(os.listdir('.')))
    # Create a list for all file types
    file_types = []
    for filename in os.listdir('.'):
        # Separate file name from file type
        names_and_types = filename.split('.')
        # Store file type in the types list
        if names_and_types[1] not in file_types:
            file_types.append(names_and_types[1])
        else:
            pass

    for file_type in file_types:
        try:
            os.mkdir(file_type)
        except FileExistsError:
            pass


main()