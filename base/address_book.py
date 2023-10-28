from collections import UserDict, defaultdict
from datetime import datetime
from helpers.weekdays import WEEKDAYS, CURRENT_DATE


class AddressBook(UserDict):
    def add_record(self, contact: dict) -> None:
        self.data[contact.name.value] = contact

    def find(self, key: str) -> object:
        res = self.data.get(key)
        return res

    def delete(self, key: str) -> None:
        del self.data[key]

    def set_birthday(self, name: str, date: str) -> None:
        contact = self.find(name)
        contact.add_birthday(date)

    def show_birthday(self, name: str) -> str:
        contact = self.find(name)

        if contact.birthday:
            return contact.birthday.value
        else:
            raise AttributeError(
                f"The birthday field is missing from {contact.name.value}'s contact"
            )

    def get_birthdays_per_week(self) -> str:
        birthday_dict = defaultdict(list)
        birthdays_info = ""

        for info in self.data.values():
            name = info.name.value.title()
            birthday = datetime.strptime(str(info.birthday), "%d %B %Y")
            birthday = birthday.date()
            birthday_this_year = birthday.replace(year=CURRENT_DATE.year)

            if birthday_this_year < CURRENT_DATE:
                birthday_this_year = birthday.replace(year=CURRENT_DATE.year + 1)

            delta_days = (birthday_this_year - CURRENT_DATE).days

            if delta_days < 7:
                if birthday_this_year.weekday() >= 5:
                    birthday_dict[WEEKDAYS[0]].append(name)
                else:
                    birthday_dict[WEEKDAYS[birthday_this_year.weekday()]].append(name)

        for day, users_list in birthday_dict.items():
            birthdays_info += f"{day}: {', '.join(list(users_list))}\n"

        return birthdays_info
