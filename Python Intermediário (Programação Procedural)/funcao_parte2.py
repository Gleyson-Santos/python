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


var = dumb()
print(id(var))
print(id(f))
if var == f:
    print("Var é igual a f")
else:
    print("Var não é igual a f")
