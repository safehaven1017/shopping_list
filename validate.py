# VALIDATE USER INPUT WHEN SELECTING NUMERICAL OPTIONS FROM A MENU

def validate_menu_selection(min, max):
    while True:
        
        # GIVES USER THE OPTION TO CHOOSE A MENU ITEM OR QUIT OUT OF LOOP
        menu_input = input("Enter your choice here. Enter 'q' to quit: ")
        # DETECTS WHETHER OR NOT USER ENTERS "Q" FOR QUIT OR CHOOSES A NUMBER
        if menu_input.isnumeric() == True or menu_input.lower() == "q":
            
            # FOR NUMERICAL INPUTS
            if menu_input.lower() != 'q':
                
                # RETURNS INPUT IF NUMERICAL INPUT IS WITHIN RANGE
                if int(min) <= int(menu_input) <= int(max):
                    return int(menu_input)
                
                # ERROR HANDLING FOR USER CHOOSING NUMBER OUTSIDE OF RANGE
                else:
                    print(f"\nInvalid number. Choose options between {min} and {max}.\n")
            
            # RETURNS INPUT WHEN USER TYPES "Q" OR "BACK" KEY
            else:
                return menu_input.lower()
        else:
            print("\nInvalid entry. Try again...\n")


# VALIDATE INPUT FOR LIST NAME
def validate_name():
    while True:
        name = input("Input a name here: ")

        # RETURNS INPUT WHEN USER TYPES "Q" OR "BACK" KEY
        if name.lower() == 'q':
            return name.lower()

        # FILTERING CHARACTERS
        test_name = name.replace("'", '')
        test_name = name.replace(" ", '')

        # VALIDATES THAT INPUT IS ALPHABETICAL
        if test_name.isalpha() == True:
            return name.upper()
        
        # ERROR HANDLING
        else:
            print("\nInvalid characters in entry.\n")


# VALIDATES ITEM UPON CREATION
def validate_item():
    while True:
        item_name = input("Input an item name here: ")

        # RETURNS INPUT WHEN USER TYPES "Q" OR "BACK" KEY
        if item_name.lower() == 'b':
            return item_name.lower()

        elif item_name.lower() != 'b':
            # FILTERING CHARACTERS
            test_name = item_name.replace("'", '')
            test_name = item_name.replace(" ", '')

            # VALIDATES THAT INPUT IS ALPHABETICAL, ITEMS SHOULD BE CAPITALIZED (TITLE)
            if test_name.isalpha() == True:
                return item_name.title()

        # ERROR HANDLING
        else:
            print("\nInvalid characters in entry. Make sure you don't enter symbols or numbers.\n")

