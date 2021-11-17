from validate import validate_item


# ADD ITEM TO ITEMS LIST IN DICTIONARY
def add_items(dict):
    while True:
        item_input = validate_item()
        if item_input == "b":
            break
        else:
            for key in dict:
                dict[key].append(item_input)
                print(dict)
    