"""
while/else
contadores
acumuladores
"""
contador = 1
acumulador = 1
while contador <= 10:
    print(contador, ':', acumulador)

    if contador > 5:
        break

    acumulador += contador
    contador += 1
else:
    print('Entrou no else')
print('Isso sera executado !!!')
