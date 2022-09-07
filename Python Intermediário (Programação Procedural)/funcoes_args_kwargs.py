"""
Funções (def) em Python - *args **args
"""


def func(*args, **kwargs):
    args = list(args)
    print(args)
    print(args[0])
    print(args[-1])


func(1, 2, 3, 4, 5)
