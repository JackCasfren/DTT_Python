
import sys, os
# import the interactions for each section of the API.
import interactions.full_pantry as full_pantry
import interactions.full_basket as full_basket


#* START OF THE CLI CODE:
def main():
    #start puting in here the CLI stuff
    # TODO CLI
    
    print("""
    Welcome to the Pantry CLI!
    Type 'help' for a list of commands. Type 'exit' to quit.
    These are the options:
    Pantry interactions:
    [1] get_pantry_data
    [2] update_pantry_account
    Basket Interactions:
    [3] 
    [4] 
    [5] 
    [6] 
    [7]
    """)


    
    while True:
        command = input("> ")
        match command:
            case "exit" | "e":
                break
            case "help" | "h":
                print("Available commands: exit, help")
            
            case "get_pantry_data" | "1":
                print(full_pantry.get_pantry_data())
            case "get_pantry_data" | "2":
                print("We would recomend not changing this. for now it break many things")
                print("insert the name and the descrption")
                name = input("> ")
                description = input("> ")
                print(full_pantry.update_pantry_account(name,description ))







            case _:
                print("Invalid command.")
                



if __name__ == "__main__":
    main()




