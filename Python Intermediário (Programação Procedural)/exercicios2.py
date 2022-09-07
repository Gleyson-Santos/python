"""
1 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor
da função2 executada
"""


# def func1():
#     x = int(input('Digite um número: '))
#     y = int(input('Digite outro número: '))
#     return x + y
#
#
# def func2(arg):
#     return arg()
#
# var = func2(func1)
# print(var)

"""
2 - Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2
executada. Faça a função1 executar duas funções que recebam um número
diferente de argumentos.
"""


def mestre(func, *args, **kwargs):
    return func(*args, **kwargs)


def fala_oi(nome, *msg2):
    return f'Oi {nome} {msg2}'


def saudacao(nome, msg):
    return f'{msg} {nome}'


executando = mestre(fala_oi, 'Gleyson', 'outra msg', 'mais msg', '2', '3')
executando2 = mestre(saudacao, 'Gleyson', 'Bom dia')
print(executando)
print(executando2)
