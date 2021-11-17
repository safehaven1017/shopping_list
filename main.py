import os
from validate import validate_menu_selection
from edit_lists import edit_lists
from view_lists import view_lists

def main():
    
    # creating function to clear console
    clear = lambda: os.system('clear')

    # create storage for shopping lists
    shopping_lists = []

    while True:
        print("\nSHOPPING HELPER")
        print("---------------\n")
        print("1. CREATE SHOPPING LISTS")
        print("2. EDIT SHOPPING LISTS")
        print("3. DELETE SHOPPING LISTS")
        print("4. VIEW SHOPPING LISTS\n")
        
        # get user input
        user_input = validate_menu_selection(1, 4)

        # create shopping lists
        if user_input == 1:
            clear()
            shopping_lists = shopping_lists + edit_lists()  
            # edit_lists(shopping_lists)      

        # edit shopping lists
        elif user_input == 2:
            clear()
            edit_lists(shopping_lists)

        # delete shopping lists
        # elif user_input == 3:
        #     clear()
        #     delete_lists(shopping_lists)
        
        # view shopping lists
        elif user_input == 4:
            clear()
            view_lists(shopping_lists)
        # quit
        else:
            clear()
            quit()

main()



