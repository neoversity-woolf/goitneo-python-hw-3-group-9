from datetime import datetime
from base.field import Field


class Birthday(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value, expected_format="%d.%m.%Y"):
        try:
            parsed_date = datetime.strptime(value, expected_format)
            self.__value = parsed_date.strftime("%d %B %Y")
        except ValueError:
            print("The date format is not 'DD.MM.YYYY'")
