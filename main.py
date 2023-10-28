from base.address_book import AddressBook
from base.record import Record
from helpers.decorator import input_error
from helpers.input_parser import parse_input


@input_error
def add_contact(args: list, contacts: dict) -> str:  # cmd add[ім'я][телефон]
    name, phone = args

    record = Record(name)
    record.add_phone(phone)
    contacts.add_record(record)
    print("🟢 Contact added")


@input_error
def update_contact(args: list, contacts: dict) -> None:  # cmd change[ім'я][телефон]
    name, old_phone, new_phone = args
    search_record = contacts.find(name)
    search_record.edit_phone(old_phone, new_phone)
    print("🟠 Contact updated")


@input_error
def get_contact(args: list, contacts: dict) -> str:  # cmd phone[ім'я]
    search_name = str(args[0])

    contacts.find(search_name)

    for name, phone in contacts.items():
        if search_name == name:
            return f"📍 : {search_name.title()} 📱 {phone}"
        else:
            return f"⛔️ Contact {search_name.title()} doesn't exist"


@input_error
def get_all_contacts(contacts: dict) -> None:  # cmd all
    phonebook = "*** {:^20} ***\n\n".format("📒 Phonebook")

    for name, info in contacts.items():
        phones = ""
        for phone in info.phones:
            phones += str(phone)
        phonebook += "📍 Contact: {:<10} 📱 {:<10}\n".format(name.title(), phones)

    print(phonebook)


@input_error
def set_birthday(args: list, contacts: dict) -> None:  # cmd add-birthday[ім'я][д.н.]
    name, b_date = args
    contacts.set_birthday(name, b_date)
    print("🎉 Birthday added")


@input_error
def show_birthday(args: list, contacts: dict) -> None:  # cmd show-birthday[ім'я]
    name = str(args[0])
    contact_bday = contacts.show_birthday(name)
    print(contact_bday)


def happy_birthdays(contacts: dict) -> None:  # cmd birthdays
    birthdays = contacts.get_birthdays_per_week()
    print(birthdays)


def main():
    book = AddressBook()
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
            add_contact(args, book)
        elif command == "change":  # update contact from phonebook
            update_contact(args, book)
        elif command == "phone":  # get contact from phonebook
            search_name = str(args[0])
            search_contact = book.find(search_name)
            print(search_contact)
        elif command == "all":  # get all contacts from phonebook
            get_all_contacts(book)
        elif command == "add-birthday":  # add birthday to contact
            set_birthday(args, book)
        elif command == "show-birthday":  # show contact birthday
            show_birthday(args, book)
        elif command == "birthdays":  # show contacts birthday for next week
            happy_birthdays(book)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
