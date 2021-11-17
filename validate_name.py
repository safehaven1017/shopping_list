def validate_name():
    while True:
        name = input("Input a name here: ")

        if name.lower() == 'q':
            return name.lower()

        # filtering characters
        test_name = name.replace("'", '')
        test_name = name.replace(" ", '')

        # validation statements
        if test_name.isalpha() == True:
            return name.upper()
        else:
            print("\nInvalid characters in entry.\n")