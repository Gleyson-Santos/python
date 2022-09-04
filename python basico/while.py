"""
while em Python
utilizado para realizar ações enquanto uma condição for verdadeira.
"""
# x = True
x = 0  # coluna

while x < 5:
    # break
    sair = input('Deseja sair? s/n')
    if sair == 's':
        break
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    op = input('Digite um operador: ')

    if not n1.isnumeric() or not n2.isnumeric():
        print('Você precisa digitar um número ou sair\n')
        continue

    n1 = int(n1)
    n2 = int(n2)

    if op == '+':
        print(n1 + n2)
    elif op == '-':
        print(n1 - n2)
    elif op == '*':
        print(n1 * n2)
    elif op == '/':
        print(n1 / n2)
    else:
        print('Bye Bye')
