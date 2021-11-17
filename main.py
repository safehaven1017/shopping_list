import os
import validate_menu_selection
import create_lists

def main():
    
    # creating function to clear console
    clear = lambda: os.system('clear')

    # create storage for shopping lists
    shopping_lists = []

    while True:
        print("SHOPPING HELPER")
        print("---------------\n")
        print("1. CREATE SHOPPING LISTS")
        print("2. DELETE SHOPPING LISTS")
        print("3. VIEW SHOPPING LISTS")
        
        # get user input
        user_input = validate_menu_selection(1, 5)

        # create shopping lists
        if user_input == 1:
            clear()
            add_to_shopping_lists = []
            add_to_shopping_lists = add_to_shopping_lists + create_lists()        

        # create shopping lists
        elif user_input == 2:
            clear()
            edit_lists(shopping_lists)

        # delete shopping lists
        elif user_input == 3:
            clear()
            delete_lists(shopping_lists)
        
        # view shopping lists
        elif user_input == 4:
            clear()
            view_lists(shopping_lists)
        # quit
        else:
            clear()
            quit()



