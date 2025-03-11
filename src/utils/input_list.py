def input_list():
    output = input('Digite os números (separados por espaço): ')
    values = output.split(' ')
    numbers = []

    for number in values:
        numbers.append(float(number))

    return numbers
