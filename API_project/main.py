
import sys, os
# import the interactions for each section of the API.
import interactions.full_pantry as full_pantry
import interactions.full_basket as full_basket


#* START OF THE CLI CODE:
def main():
    #start puting in here the CLI stuff
    # TODO finish CLI
    
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
            case "exit" | "e" :
                break
            case "help" | "h":
                print("Available commands: exit, help")
            
            case "get_pantry_data" | "1":
                # TODO format this correctly.
                print(full_pantry.get_pantry_data())
                

            case "get_pantry_data" | "2":
                print("We would recomend not changing this. for now it break many things")
                print("insert the name and the descrption")
                name = input("Name: ")
                description = input("Description: ")
                # todo format the json it appears with tabs and not a straight line
                print(full_pantry.update_pantry_account(name,description ))
            # the basket interactions:
            case "3":
                print("basket 3")
            case "4":
                print("basket 4")
            case "5":
                print("basket 5")
            case "6":
                print("basket 6")
            case "7":
                print("basket 7")

            case _:
                print("Invalid command.")
                



if __name__ == "__main__":
    main()




