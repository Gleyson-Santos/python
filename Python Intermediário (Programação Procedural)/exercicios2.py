"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor
da função2 executada
"""


def func1():
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))
    return x + y


def func2(arg):
    return arg()

var = func2(func1)
print(var)

"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2
executada. Faça a função1 executar duas funções que recebam um número
diferente de argumentos.
"""


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, msg):
    return f'{msg} {nome}'
