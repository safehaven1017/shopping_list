# PRINT ALL SHOPPING
def view_lists(shopping_lists):
    print()
    
    # COUNT USED TO PRINT INDEX
    count = 0
    for dict in shopping_lists:
        for key in dict:
            count += 1
            list_string_concat = f"{count} - {key}:"
            for items in range(len(dict[key])):
                list_string_concat = list_string_concat + f" {dict[key][items]},"
            list_string_concat = list_string_concat[:-1]
            print(list_string_concat)