"""
for / else em Python
"""
variavel = ['Luiz Otávio', 'Joãozinho', 'Maria']

comeca_com_j = False
for valor in variavel:
    if valor.lower().startswith('j'):
        print(valor, 'começa com J')
    else:
        print(valor, 'não começa com J')

