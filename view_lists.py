def view_lists(entries):
    print()
    
    # create count to show index next to entry 
    count = 1

    # print all entries 
    for entry in entries:
        for dict in entry:
            print(f"{count} - List Name: {dict} - Items: {entry[dict]}")
        count += 1