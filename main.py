import os
from validate import validate_menu_selection
from lists import *

def main():
    
    # CREATING FUNCTION TO CLEAR CONSOLE
    clear = lambda: os.system('clear')

    # CREATE STORAGE FOR SHOPPING LISTS
    shopping_lists = []

    while True:
        
        print("\nSHOPPING HELPER")
        print("---------------\n")
        print("1. CREATE SHOPPING LISTS")
        print("2. EDIT SHOPPING LISTS")
        print("3. DELETE SHOPPING LISTS")
        print("4. VIEW SHOPPING LISTS\n")
        
        # GET USER INPUT
        user_input = validate_menu_selection(1, 4)

        # CREATE SHOPPING LISTS
        if user_input == 1:
            clear()
            shopping_lists += edit_lists(shopping_lists, n=True)

        # edit shopping lists
        elif user_input == 2 and shopping_lists != []:
            clear()
            new_list = edit_lists(shopping_lists)
            shopping_lists = new_list
        elif user_input == 2 and shopping_lists == []:
            print("\nThere are no lists to edit!\n")
        # delete shopping lists
        # elif user_input == 3:
        #     clear()
        #     delete_lists(shopping_lists)
        
        # VIEW SHOPPING LISTS
        elif user_input == 4:
            clear()
            view_lists(shopping_lists)
            # print(shopping_lists)
        # QUIT
        else:
            clear()
            quit()

main()



