from validate_name import validate_name

def edit_lists(shopping_list):

    # creating temp dictionary and list
    temp_shopping_dict = {}
    temp_shopping_list = []

    while True:
        if len(shopping_list) > 0:
            return
        else:
            # validate shopping list name
            print("""Enter a name for your shopping list. 
            Go back to the menu anytime by entering 'q'.""")
            name_input = validate_name()
            if name_input == 'q':
                break
            
            # add items to list
            print("""Enter an item name to add it to your list. 
            Go back to the menu anytime by entering 'q'.""")
            phone_input = validate_phone()
            if phone_input == 'q':
                break

            # assigning input to list/dict 
            temp_shopping_dict[name_input] = phone_input
            temp_shopping_list.append(temp_shopping_dict)

    return temp_shopping_list


