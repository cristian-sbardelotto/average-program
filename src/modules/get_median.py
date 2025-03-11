from utils.input_list import input_list
from utils.format_int import format_int


def get_median():
    numbers = input_list()
    numbers.sort()

    if (len(numbers) % 2 != 0):
        median = numbers[int(len(numbers) / 2)]
        return print(f'A mediana é {format_int(median)}')

    first_median = numbers[int(len(numbers) / 2) - 1]
    second_median = numbers[int(len(numbers) / 2)]

    median = (first_median + second_median) / 2
    formatted_median = format_int(median)

    print(f'A mediana é {formatted_median}')
