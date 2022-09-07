"""
Funções (def) em Python - *args **args
"""


def func(*args, **kwargs):
    print(args)
    # print(kwargs['nome'], kwargs['sobrenome'])
    idade = kwargs.get('idade')
    print(idade)

lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Gleyson', sobrenome='Santos', idade=0)
