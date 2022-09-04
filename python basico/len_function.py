"""
len() conta a quantidade de characteres em um string ou lista
não funciona com int, float ou bool
"""

user = input('Digite seu usuário.\n')
qtd_chars = len(user)

if qtd_chars < 6:
    print('Você precisa digitar pelo menos, 06 chars')
else:
    print('Você foi cadastrado no sistema. ')
