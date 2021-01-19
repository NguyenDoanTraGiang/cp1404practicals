import shutil
import os


def main():
    print("Starting directory is: {}".format(os.getcwd()))
    # Change to desired directory
    os.chdir('FilesToSort')
    # Print all file in current directory
    print("All file in current directory is {}".format(os.listdir('.')))

    for filename in os.listdir('.'):
        # Ignore directories
        if os.path.isdir(filename):
            continue
        # Separate file name from file type
        names_and_types = filename.split('.')
        # Create directories based on file types
        try:
            os.mkdir(names_and_types[1])
        except FileExistsError:
            pass

        # Move files to subdirectories
        shutil.move(filename, names_and_types[1])


main()
