from items import *
from validate import *
from view_lists import view_lists

def edit_lists(shopping_list=[]):

    # creating temp dictionary and list
    temp_shopping_dict = {}
    temp_shopping_list = []

    while True:
        # if given lists, display lists and give edit options
        if len(shopping_list) > 0:
            view_lists(shopping_list)

            # ask for user input
            print("\nChoose a list to edit, or create new list.")
            edit_input = validate_menu_selection(1, len(shopping_list))
            if edit_input == "q":
                break
            else:
                temp_shopping_dict = shopping_list[edit_input - 1]
                add_items(temp_shopping_dict)
               
        # create list if not given one
        else:
            # validate shopping list name
            print("Enter a name for your new shopping list.") 
            print("Go back to the menu by entering 'q'.")
            name_input = validate_name()
            if name_input == 'q':
                break
            # initialize first list
            else:
                temp_item_list = []
                temp_shopping_dict[name_input] = temp_item_list
                temp_shopping_list.append(temp_shopping_dict)
                
                # run edit list function
                edit_lists(temp_shopping_list)
                break
           
    return temp_shopping_list


