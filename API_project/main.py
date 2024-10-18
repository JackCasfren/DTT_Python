
import sys, os, json
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
    [3] get_pantry_data
    [4] make_pantry_insert
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
                # todo make proper help section
                print("Available commands: exit, help")
            
            case "get_pantry_data" | "1":
                
                print(full_pantry.get_pantry_data())
                

            case "get_pantry_data" | "2":
                # todo allow the user to escape this option incase they accessed accidentaly
                print("We would recomend not changing this. for now it break many things")
                print("insert the name and the descrption")
                name = input("Name: ")
                description = input("Description: ")
                # todo format the json it appears with tabs and not a straight line
                print(full_pantry.update_pantry_account(name,description ))
            
            #* the basket interactions:


            case "3":
                # todo add list of all of the baskets
                #! working on it!
                full_pantry.list_all_baskets()
                
                print("What is the name of the basket you read?")
                sel_pantry = input("Name: ").lower()
                print(full_basket.get_basket_data(sel_pantry))
            case "4":
                # todo UX to allow user to insert data
                # could be allowing the user to make their won json structure
                # or it could be just adding values inside a json structure 
                # for now im going to go for the second option.
                print("Insert values into a basket selected.")
                print("Into what basket do you want to insert?")
                full_pantry.list_all_baskets()
                # todo proper function to make new baskets
                sel_pantry = input("Name: ").lower()
                '''print(insert the following data: )
                input(name: )
                input(product )
                input(main_color )
                input(Logo_shape )
                input(industry )
                input(usage )
                input(additional_features )
                '''
                
                '''
                {
                    "company": {
                        "name": "Microsoft",
                        "product": "Windows10",
                        "main_color": "blue",
                        "Logo_shape": "window",
                        "industry": "Software",
                        "usage": "Cloud",
                        "additional_features": []
                    }
                }

                '''
                # Collect input from the user
                company_name = input("Insert the company name: ")
                product = input("Insert the product: ")
                main_color = input("Insert the main color: ")
                logo_shape = input("Insert the logo shape: ")
                industry = input("Insert the industry: ")
                usage = input("Insert the usage: ")
                additional_features = input("Insert additional features (separated by commas): ").split(',')

                # Create the JSON structure
                data = {
                    "company": {
                        "name": company_name,
                        "product": product,
                        "main_color": main_color,
                        "Logo_shape": logo_shape,
                        "industry": industry,
                        "usage": usage,
                        "additional_features": [feature.strip() for feature in additional_features if feature.strip()]
                    }
                }

                # Convert the dictionary to JSON and print it
                json_data = json.dumps(data, indent=4)
                print(json_data)

                full_basket.make_pantry_insert(sel_pantry, new_data )


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




