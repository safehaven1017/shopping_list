from validate_name import validate_name
from validate_phone import validate_phone

def add_entry():

    # creating temp dictionary and list
    temp_contact_dict = {}
    temp_contact_list = []

    while True:
        # validate name
        name_input = validate_name()
        if name_input == 'q':
            break
        
        # validate phone
        phone_input = validate_phone()
        if phone_input == 'q':
            break

        # assigning input to list/dict 
        temp_contact_dict[name_input] = phone_input
        temp_contact_list.append(temp_contact_dict)

    return temp_contact_list


