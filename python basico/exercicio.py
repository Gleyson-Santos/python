"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro

numero_inteiro = input('Digite um número inteiro\n')
if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)
    if numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} é Par')
    else:
        print(f'{numero_inteiro} é Impar')
else:
    print('Não é um número inteiro!!!')
"""

"""
Faça um programa que pergunte a hora ao usuário e baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa Tarde 12-17 e Boa noite 18-23.
"""
horario = input("Digite um horario\n")
if horario.isdigit():
    horario = int(horario)
    if horario > 0 < 24:
        print('Bom dia' if horario < 11
              else 'Boa tarde' if horario < 17
              else 'Boa Noite')
    else:
        print('Digite um horario entre 0 e 23')
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome pe normal"; maior que 6 escreva "Seu nome é muito grande".
"""