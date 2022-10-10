"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:

Se um lista for maior que a outra, a soma só vai considerar o tamanho da
menor.

Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

======================resultado
lista_soma = [2, 4, 6, 8]
"""
from itertools import zip_longest

lista_a = [1, 2, 3, 44, 5, 6, 7]
lista_b = [10, 2, 3, 4]
lista_soma = [(x+y) for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
# for x, y in zip(lista_a, lista_b):
#     lista_soma.append(x + y)
print(lista_soma)
