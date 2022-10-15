def divide(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser zero')
    return n1 / n2

try:
    print(divide(9, 0))
except ValueError as error:
    print('Você esta tentando dividir por 0', error)
