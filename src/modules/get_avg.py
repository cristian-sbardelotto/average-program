from utils.input_list import input_list
from utils.format_int import format_int


def get_average():
    numbers = input_list()

    average = sum(numbers) / len(numbers)
    formatted_average = format_int(average)

    print(f'A média é {formatted_average}')
