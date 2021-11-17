from validate import validate_item
from view import view_dictionary

# ADD ITEM TO ITEMS LIST IN DICTIONARY
def add_items(dict):
    while True:
        item_input = validate_item()
        if item_input == "b":
            break
        else:
            for key in dict:
                dict[key].append(item_input)
                view_dictionary(dict)


# REMOVE ITEM TO ITEMS LIST IN DICTIONARY
def remove_items(dict):
    while True:
        item_input = validate_item()
        if item_input == "b":
            break
        else:
            for key in dict:
                if item_input not in dict[key]:
                    print(f"The item '{item_input}' wasn't found in this list. Try again.")
                else:
                    dict[key].remove(item_input)
                    view_dictionary(dict)

    