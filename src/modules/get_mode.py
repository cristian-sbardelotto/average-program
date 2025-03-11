from utils.input_list import input_list
from utils.format_int import format_int


def get_mode():
    numbers = input_list()
    numbers.sort()

    times_appeared = [0]
    mode = [0]
    unique_values = set(numbers)

    for value in unique_values:
        times_value_appeared = numbers.count(value)

        if (times_value_appeared > times_appeared[0]):
            times_appeared.clear()
            mode.clear()
            times_appeared.append(times_value_appeared)
            mode.append(format_int(value))
        elif times_value_appeared == times_appeared[0]:
            times_appeared.append(times_value_appeared)
            mode.append(format_int(value))

    print(f'A moda é {mode}')
