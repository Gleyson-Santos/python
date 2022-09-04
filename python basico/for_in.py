"""
For in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""
texto = 'Python'
z, indice = 0, len(texto)
# while c < indice:
#     print(texto[c])
#     c += 1
# print()
# for n, letra in enumerate(texto):
#     print(n, ':', letra)
# for x in range(-20, 1, 1):
#     print(x)
#
# for x in range(0, 100, 8):
#     print(x)
nova_string = ''
for letra in texto:
    if letra == 't':
        nova_string += letra.lower()
    else:
        nova_string += letra
print(nova_string)

a, b, c = 1, 2, 3

a, b, c = c, b, a

print(a, b, c)
