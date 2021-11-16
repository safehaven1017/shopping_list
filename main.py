import os

def main():
    
    # creating function to clear console
    clear = lambda: os.system('clear')

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
            create_lists(shopping_lists)

        # delete shopping lists
        elif user_input == 2:
            clear()
            delete_lists(shopping_lists)
        
        # view shopping lists
        elif user_input == 3:
            clear()
            view_lists(shopping_lists)
        # quit
        else:
            clear()
            quit()



