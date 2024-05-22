# App1 - Functions.py
#-------------------------------------------------------------------------------------
import os
import sys


# Function to determine the base directory of the executable
def get_base_dir():
    # If the application is frozen using PyInstaller
    if getattr(sys, 'frozen', False):
        # Use the sys.executable path
        return os.path.dirname(sys.executable)
    # If the application is running in a normal Python environment
    else:
        # Use the path of the script file
        return os.path.dirname(os.path.abspath(__file__))


# Use the base directory to construct the path to 'todos.txt'
base_dir = get_base_dir()
todos_path = os.path.join(base_dir, 'todos.txt')

# Check if 'todos.txt' exists, create if it does not
if not os.path.exists(todos_path):
    with open(todos_path, 'w') as file:
        pass


# Custom function 1: Single Argument / Parameter - (default arg)
def get_todos(filepath=todos_path):
    """ Open file, read file & store data in var todos."""
    with open(filepath, "r") as file_local:              # "D6_App1_File33_todos.txt"
        todos_local = file_local.readlines()
    return todos_local


# Custom function 2: Multiple Argument / Parameters - (non-default, default arg)
def write_todos(todos_arg, filepath=todos_path):
    """ Open file, write file & store data in var todos."""
    with open(filepath, "w") as file:                    # "D6_App1_File33_todos.txt"
        file.writelines(todos_arg)


#-------------------------------------------------------------------------------------

# Best Practice:
# Below code prints output only when it is executed in function file - explicitly
# Adding this code line helps to test functions during development phase

if __name__ == "__main__":
    print("x")
    print(get_todos())
    print(__name__)
