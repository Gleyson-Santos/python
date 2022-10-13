"""
tratando excessões
"""

try:
    print(a)
except NameError as erro:
    print(f'Erro: {erro}')

print('Bora continuar!!!')
