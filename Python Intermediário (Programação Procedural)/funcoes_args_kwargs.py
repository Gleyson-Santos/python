"""
Funções (def) em Python - *args **args
"""


def func(a1, a2, a3, a4, a5, nome=None, a6=None):
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print(a5)
    print(a6)
    print(nome)
    return nome, a6


var = func(1, 2, 3, 4, 5, nome='Gleyson')
print(var[0])
