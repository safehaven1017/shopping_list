def validate_menu_selection(min, max):
    while True:
        menu_input = input("Enter your choice here. Enter 'q' to quit: ")
        if menu_input.isnumeric() == True or menu_input.lower() == "q":
            if menu_input.lower() != 'q':
                if int(min) <= int(menu_input) <= int(max):
                    return int(menu_input)
                else:
                    print(f"\nInvalid number. Choose options between {min} and {max}.\n")
            else:
                return menu_input.lower()
        else:
            print("\nInvalid entry. Try again...\n")