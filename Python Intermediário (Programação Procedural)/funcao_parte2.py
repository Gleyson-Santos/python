"""
Funções - def em Python (Parte 2)
"""


# def divisao(n1, n2):
#     return [n1, n2]
#
# divide = divisao(n1=0, n2=0)
# if divide:
#     print(divide)

def f(var):
    print(var)


def dumb():
    return f


var = dumb()('Valor passado para função f')
print(var)
