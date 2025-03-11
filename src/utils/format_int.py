def format_int(number: int | float):
    if (number.is_integer()):
        return int(number)
    return number
