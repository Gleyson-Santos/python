"""
Formatando valores com modificadores - Aula 5

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)
> - esquerda
< - direita
^- centro
"""
num1 = 10
num2 = 3
divisao = num1 / num2
# print('{:.2f}'.format(divisao))
# print(f'{divisao:.2f}')

nome = 'Luiz Otavio'
# print(f'{nome:s}')

num1 = 1
# print(f'{num1:0>10}')

num2 = 1150
"""
print(f'{num2:0<10} zeros a direita')
print(f'{num2:0^10} número no centro')
print(f'{num2:0>10.2f} zero a esquerda e dois pontos decimais')
"""

nome = "Otávio Miranda"
# print(f' {nome:#^50}')
nome_formatado = f"{nome:#^15}"
print(nome_formatado)
