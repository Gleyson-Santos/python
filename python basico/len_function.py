"""
len() conta a quantidade de characteres em uma string ou lista
não funciona com int, float ou bool
"""

user = input('Digite seu usuário.\n')
qtd_chars = len(user)

if qtd_chars < 6:
    print('Você precisa digitar pelo menos, 06 chars')
else:
    print('Você foi cadastrado no sistema. ')

str1 = input('Digite alguma coisa: ')
str2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitados foi {len(str1) + len(str2)}')

