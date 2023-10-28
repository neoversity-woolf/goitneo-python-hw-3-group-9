from base.field import Field


class Phone(Field):
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        has_ten_symbols = len(value) == 10
        is_digit = value.isdigit()

        if has_ten_symbols and is_digit:
            self.__value = value
        else:
            raise ValueError("Field phone is incorrect")
