def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            print("Give me name and phone please.")
        except IndexError:
            print("Sorry. Contact book is empty.")
        except TypeError:
            print("Wrong value for operation.")
        except AttributeError:
            print("Wrong value for operation.")

    return inner
