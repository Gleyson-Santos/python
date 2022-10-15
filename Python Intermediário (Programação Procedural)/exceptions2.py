def converte_numero(valor):
    try:
        valor = int(valor)
        return valor
    except ValueError as erro:
        try:
            valor = float(valor)
            return valor
        except ValueError:
            pass
true = True
while true:
    numero = converte_numero(input('Digite um número: '))
    if numero is None:
        print('Erro')
    else:
        print(numero + 5)
        sair = input('Quer somar de novo? s/n ')
        if sair == 'n':
            break
