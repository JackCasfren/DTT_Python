
import sys, os
# Add the path to the interactions directory (sry, NIX can sometimes mess this up so im cheking)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ''))
sys.path.append(os.path.join(project_root, 'interactions'))

# Import the function you need
from full_pantry import *
from full_basket import *


#* START OF THE CLI CODE:
def main():
    #start puting in here the CLI stuff
    # TODO CLI
    
    print("Welcome to the Pantry CLI!")
    print("Type 'help' for a list of commands. Type 'exit' to quit.")

    while True:
        command = input("> ")
        match command:
            case "exit":
                break
            case "help":
                print("Available commands: exit, help")
            
            case "get_pantry_data":
                print(full_pantry.get_pantry_data())
            case _:
                print("Invalid command.")
                



if __name__ == "__main__":
    main()




