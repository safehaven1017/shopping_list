from items import *
from validate import *
from view import view_lists

def edit_lists(main_list, n=False):

    # CREATING TEMP DICTIONARY AND LIST
    temp_shopping_dict = {}
    temp_shopping_list = []

    while True:
        # IF GIVEN LISTS, DISPLAY LISTS AND GIVE USER OPTIONS
        if n == False:
            temp_shopping_list = main_list
            view_lists(main_list)

            # ASK FOR USER INPUT
            print("\nChoose the corresponding number of a list to edit it, or create new list with 'n'.")
            edit_input = validate_menu_selection(1, len(main_list))
            # SAVE SHOPPING LIST AND GO BACK TO MAIN MENU
            if edit_input == "q":
                if len(temp_shopping_list) > 0:
                    return temp_shopping_list
            # CREATE NEW LIST
            elif edit_input == "n":
               edit_lists(temp_shopping_list,n=True) 
            #EDIT LIST 
            else:
                print("\nEnter '1' to add or '2' to remove items from list.")
                items_input = validate_menu_selection(1, 2)
                # ADD ITEMS
                if items_input == 1:
                    temp_shopping_dict = main_list[edit_input - 1]
                    add_items(temp_shopping_dict)
                # REMOVE ITEMS
                elif items_input == 2:
                    if len(main_list[edit_input - 1]) < 1:
                        temp_shopping_dict = main_list[edit_input - 1]
                        remove_items(temp_shopping_dict)
                    else:
                        print("\nNo items to remove.\n")
               
        # CREATE LIST IF NOT GIVEN ONE
        else:
            # VALIDATE SHOPPING LIST NAME
            print("Enter a name for your new shopping list.") 
            print("Go back to the menu by entering 'q'.")
            name_input = validate_name()
            if name_input == 'q':
                break
            # INITIALIZE AND SAVE FIRST LIST
            else:
                temp_item_list = []
                temp_shopping_dict[name_input] = temp_item_list
                temp_shopping_list.append(temp_shopping_dict)
                return temp_shopping_list