"""
Operadores Lógicos - Meu Cursinho de Python 3
and, or, not, in e not in
"""
nome = 'gleyson'

user = input('nome do user:\n')
senha = input('Senha do user: \n')

usuario_bd = 'gleyson'
senha_bd = '1234'

if user == usuario_bd and senha == senha_bd:
    print('Logado')
else:
    print('Não logado')
