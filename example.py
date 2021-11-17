shopping_list= [{'Fiesta':
                    ['milk','soda','fish']}, 
                {'Walmart': 
                    ['paper', 'napkins', 'plate', 'chips']}, 
                {'Sams Club':
                    ['chicken', 'beef', 'eggs', 'sugar', 'salt', 'pepper', 'honey']}]


for dict in shopping_list:
    for item_list in dict:
        long_string = item_list + ":"
        for items in range(len(dict[item_list])):
            long_string = long_string + f" {dict[item_list][items]},"
        print(long_string)
            