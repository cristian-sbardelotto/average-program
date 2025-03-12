from modules.get_avg import get_average
from modules.get_mode import get_mode
from modules.get_median import get_median

print("""
1. Calcular média aritmética
2. Calcular moda
3. Calcular mediana
""")

option = int(input('Escolha uma opção (digite o número correspondente): '))

match option:
    case 1:
        get_average()
    case 2:
        get_mode()
    case 3:
        get_median()
    case _:
        print('Opção inválida!')
