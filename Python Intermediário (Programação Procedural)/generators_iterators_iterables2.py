# list, tuple, str -> iteraveis
nome = 'Gleyson'  # iteravel
iterador = iter(nome)  # iterador
gerador = (letra for letra in nome)  # gerador

print(next(gerador))
print(next(gerador))
print(next(gerador))

print('after generator')
for x in gerador:
    print(x)

print('-' * 25)
try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))

except:
    ...
print('after iteration')

for letra in iterador:
    print(letra)
