from functools import wraps


class InvalidTypeError(Exception):

    """
    Custom exception raised when an invalid type is received.
    """

    def __init__(self, message):
        super().__init__(message)


def type_check(correct_type):

    """
    Decorator that checks the type of a function argument.
    :param correct_type: The correct type of the input argument.
    :return: function: A decorated function that checks if the input argument has the correct type.
    :raise: InvalidTypeError: If the type of the argument is not equal to the expected type.
    """

    def decorator(func):
        @wraps(func)
        def wrapper(arg):
            if type(arg) != correct_type:
                raise InvalidTypeError(f"received invalid type!\n{type(arg)} != {correct_type}")
            return func(arg)

        return wrapper

    return decorator


@type_check(int)
def squared_num(num):
    """
    The function takes a integer and returns integer**2
    :param num: The number to be squared
    :return: squared input
    """
    return num ** 2


if __name__ == "__main__":
    print(squared_num(3))
    print(squared_num("5"))
