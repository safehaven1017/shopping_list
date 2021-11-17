from items import *
from validate import *
from view import view_lists

def edit_lists(shopping_list=[]):

    # CREATING TEMP DICTIONARY AND LIST
    temp_shopping_dict = {}
    temp_shopping_list = []

    while True:
        # IF GIVEN LISTS, DISPLAY LISTS AND GIVE USER OPTIONS
        if len(shopping_list) > 0:
            view_lists(shopping_list)

            # ASK FOR USER INPUT
            print("\nChoose the corresponding number of a list to edit it, or create new list.")
            edit_input = validate_menu_selection(1, len(shopping_list))
            # BACK
            if edit_input == "q":
                break
            # CREATE NEW LIST
            elif edit_input == "n":
               edit_lists() 
            #EDIT LIST 
            else:
                print("\nEnter '1' to add or '2' to remove items from list.")
                items_input = validate_menu_selection(1, 2)
                # ADD ITEMS
                if items_input == 1:
                    temp_shopping_dict = shopping_list[edit_input - 1]
                    add_items(temp_shopping_dict)
                # REMOVE ITEMS
                elif items_input == 2:
                    temp_shopping_dict = shopping_list[edit_input - 1]
                    remove_items(temp_shopping_dict)
               
        # CREATE LIST IF NOT GIVEN ONE
        else:
            # VALIDATE SHOPPING LIST NAME
            print("Enter a name for your new shopping list.") 
            print("Go back to the menu by entering 'q'.")
            name_input = validate_name()
            if name_input == 'q':
                break
            # INITIALIZE FIRST LIST
            else:
                temp_item_list = []
                temp_shopping_dict[name_input] = temp_item_list
                temp_shopping_list.append(temp_shopping_dict)
                
                # RUN EDIT LIST FUNCTION
                edit_lists(temp_shopping_list)
                break
           
    return temp_shopping_list