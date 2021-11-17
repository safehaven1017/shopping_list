def view_entries(entries):
    print()
    
    # create count to show index next to entry 
    count = 1

    # print all entries 
    for entry in entries:
        for dict in entry:
            print(f"{count} - Contact Name: {dict} - Phone Number: {entry[dict]}")
        count += 1