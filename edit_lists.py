from validate_name import validate_name
import validate_item

def edit_lists(shopping_list):

    # creating temp dictionary and list
    temp_shopping_dict = {}
    temp_shopping_list = []

    while True:
        # if given list, give edit options
        if len(shopping_list) > 0:
            
        
        # create list if not given one
        else:
            # validate shopping list name
            print("""Enter a name for your shopping list. 
            Go back to the menu anytime by entering 'q'.""")
            name_input = validate_name()
            if name_input == 'q':
                break
            
            # add item to first list
            print("""Enter an item name to add it to your list. 
            Go back to the menu anytime by entering 'q'.""")
            item_input = validate_item()
            temp_item_list = []
            if item_input == 'q':
                break
            else:
                temp_item_list.append(item_input)
                temp_shopping_dict[name_input] = temp_item_list
                temp_shopping_list.append(temp_shopping_dict)
                
                # go into edit mode with temp list
                edit_lists(temp_item_list)
           
    return temp_shopping_list


