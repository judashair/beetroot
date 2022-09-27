import json

MENU = '''
1 - Add new entries
2 - Search by telephone number
3 - Search by first name
4 - Search by last name
5 - Search by state
6 - Search by city
7 - Update a record for a given telephone number
8 - Delete a record for a given telephone number
9 - An option to exit the program
'''


def open_phonebook():
    with open("phonebook.json", "r+") as phonebook_file:
        try:
            phonebook = phonebook_file.read()
            phonebook = json.loads(phonebook)
        except json.JSONDecodeError:
            phonebook = {}

    return phonebook


def valid_phone_number(phone_number: str):
    phone_number = phone_number.split('-')  # ['96', '123', '40', '50']
    if len(phone_number) != 4:
        print("Not valid format!")
        return False

    format_of_elements = [2, 3, 2, 2]
    for index, digits in enumerate(phone_number):

        if not format_of_elements[index] == len(digits):
            print("Not valid format!")
            return False

        if not digits.isnumeric():
            print("Only digits can be in phone number!")
            return False

    return True


def valid_first_or_last_name(name: str):
    if len(name) > 50:
        print("Too many characters!")
        return False

    if not name.isalpha():
        print("Name must contains only alphabet letters!")
        return False

    return True


def valid_city_or_state(place_name: str):
    set_of_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ- "

    if "  " in place_name:
        print("Too many spaces!")
        return False

    if len(place_name) > 50:
        print("Too many characters!")
        return False

    if (place_name[0] == "-") or (place_name[-1] == "-"):
        print("- can not be in the first place")
        return False

    for letter in place_name:
        if letter not in set_of_characters:
            print("Should only contain alphabet or -")
            return False

    return True


def correct_input(valid_func, prompt: str, hint=False):
    valid = False

    if hint:
        print(hint)

    while not valid:
        value = input(prompt)
        valid = valid_func(value)
    return value


def add_new_entry():
    phone_number = "+380-" + correct_input(valid_phone_number, "Enter phone number in next format: +380-XX-XXX-XX-XX"
                                                               "Country code by default +380 (Ukraine).\n" 
                                                               "Enter your phone number: +380-")

    first_name = correct_input(valid_first_or_last_name, "Name should be less than 50 characters and contains only letters.\n"
                                                 "Enter your first name: ").lower().title()

    last_name = correct_input(valid_first_or_last_name, "Name should be less than 50 characters and contains only letters.\n"
                                               "Enter your last name: ").lower().title()

    full_name: str = first_name + " " + last_name

    state = correct_input(valid_city_or_state, "Enter your state: ").strip()
    city = correct_input(valid_city_or_state, "Enter your city: ").strip()

    phonebook[phone_number] = {
        "first_name": first_name,
        "last_name": last_name,
        "full_name": full_name,
        "address": {
            "state": state,
            "city": city
        },
    }
    print('New contact added successfully!')
    with open("phonebook.json", "w") as phonebook_file:
        json.dump(phonebook, phonebook_file, indent=4)


def search_by(key: str, searching_for: str):
    search_result = []

    if key == "phone_number":
        if phonebook.get(searching_for):
            search_result.append(searching_for)
        return search_result

    for phone_number in phonebook.keys():
        if key in ["state", "city"]:
            if phonebook[phone_number]["address"][key] == searching_for:
                search_result.append(phone_number)

        elif phonebook[phone_number][key] == searching_for:
            search_result.append(phone_number)

    return search_result

    with open("phonebook.json", "w") as phonebook_file:
        json.dump(phonebook, phonebook_file, indent=4)


def delete_phone_number(phone_number: str, phonebook: dict):
    try:
        del phonebook[phone_number]
        print(f"Contact with phone number {phone_number} deleted.")
    except KeyError:
        print("Phone number is not exists!")

    with open("phonebook.json", "w") as phonebook_file:
        json.dump(phonebook, phonebook_file, indent=4)


def update_contact_info(phone_number: str, key: str, phonebook: str):
    try:
        phonebook[phone_number]

    except KeyError:
        print("Phone number is not exists!")

    if key == "phone_number":
        pass

    if key in ["state", "city"]:
        new_value = correct_input(valid_city_or_state, f"Enter your {key}: ").strip()
        phonebook[phone_number]["address"][key] = new_value

    if key in ["first_name", "last_name"]:
        new_value = correct_input(valid_first_or_last_name, "Name should be less than 50 characters and contains only letters.\n"
                                                            f"Enter your {key.replace('_', ' ')}: ").lower().title()
        phonebook[phone_number][key] = new_value

        contact = phonebook[phone_number]
        contact["full_name"] = contact["first_name"] + " " + contact["last_name"]

    if key == "full_name":
        new_first_name = correct_input(valid_first_or_last_name, "Name should be less than 50 characters and contains only letters.\n"
                                                            f"Enter your {key.replace('_', ' ')}: ").lower().title()

        new_last_name = correct_input(valid_first_or_last_name, "Name should be less than 50 characters and contains only letters.\n"
                                                            f"Enter your {key.replace('_', ' ')}: ").lower().title()

        contact = phonebook[phone_number]
        contact["first_name"] = new_first_name
        contact["last_name"] = new_last_name
        contact["full_name"] = contact["first_name"] + " " + contact["last_name"]

    with open("phonebook.json", "w") as phonebook_file:
        json.dump(phonebook, phonebook_file, indent=4)


def print_phonebook(phonebook: dict, key: list):
    for i in key:
        print(i, phonebook[i])


def menu():
    print(MENU)
    menu_func = {1: add_new_entry, 2: search_by, 3: search_by, 4: search_by, 5: search_by, 6: search_by,
             7: update_contact_info, 8: delete_phone_number}
    answer = int(input("Make your choice, please: "))
    while not (1 <= answer <= 9):
        print("There are no such menu choice!\n")
        answer = int(input("Enter only numbers from 1 to 9, please!: "))
    else:
        if answer == 1:
            menu_func[answer]()
        elif answer == 2:
            result = menu_func[answer]("phone_number", input("Enter the telephone number of contact, which you are searching: "))
            print_phonebook(phonebook, result)
        elif answer == 3:
            result = menu_func[answer]("first_name", input("Enter the first name of contact, which you are searching: "))
            print_phonebook(phonebook, result)
        elif answer == 4:
            result = menu_func[answer]("last_name", input("Enter the last name of contact, which you are searching: "))
            print_phonebook(phonebook, result)
        elif answer == 5:
            result = menu_func[answer]("state", input("Enter the state of contact, which you are searching: "))
            print_phonebook(phonebook, result)
        elif answer == 6:
            result = menu_func[answer]("city", input("Enter the city of contact, which you are searching: "))
            print_phonebook(phonebook, result)
        elif answer == 7:
            phone_number = input("Enter the telephone number of contact, which you are updating: ")
            result = menu_func[answer](phone_number, input("Please, input update info: first_name, last_name, full_name, "
                                             "address: state city: "), phonebook)
            print_phonebook(phonebook, [phone_number])
        elif answer == 8:
            menu_func[answer] = delete_phone_number(input("Enter the telephone number of contact, which you are deleting: "), phonebook)
        elif answer == 9:
            print("Thank you for using this program!")
            exit()
        else:
            print("Wrong input. Try again.")


phonebook = open_phonebook()

while True:
    menu()
