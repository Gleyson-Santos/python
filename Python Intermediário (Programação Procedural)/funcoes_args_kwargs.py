"""
Funções (def) em Python - *args **args
"""


def func(*args):
    print(args)


lista = [1, 2, 3, 4, 5]
print(*lista, sep='/*')
