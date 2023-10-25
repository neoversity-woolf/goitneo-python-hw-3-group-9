def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Sorry. Contact book is empty."

    return inner


def parse_input(user_input: str) -> (str, list):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "🟢 Contact added"


@input_error
def update_contact(args: list, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return "🟠 Contact updated"


@input_error
def get_contact(args: list, contacts: dict) -> str:
    search_name = str(args[0])

    for name, phone in contacts.items():
        if search_name == name:
            return f"📍 : {search_name.title()} 📱 {phone}"
        else:
            return f"⛔️ Contact {search_name.title()} doesn't exist"


def get_all_contacts(contacts: dict) -> str:
    phonebook = "*** {:^20} ***\n\n".format("📒 Phonebook")
    for name, phone in contacts.items():
        phonebook += "📍 Contact: {:<10} 📱 {:<10}\n".format(name.title(), phone)

    return phonebook


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:  # exit from function
            print("Good bye!")
            break
        elif command == "hello":  # start phonebook
            print("How can I help you?")
        elif command == "add":  # add contact to phonebook
            print(add_contact(args, contacts))
        elif command == "change":  # update contact from phonebook
            print(update_contact(args, contacts))
        elif command == "phone":  # get contact from phonebook
            print(get_contact(args, contacts))
        elif command == "all":  # get all contacts from phonebook
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
