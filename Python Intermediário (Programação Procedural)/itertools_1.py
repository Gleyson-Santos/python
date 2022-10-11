"""
count - itertools
"""

from itertools import count

contador = count()
lista1 = ['Luiz', 'João', 'Maria']
lista2 = zip(contador, lista1)

print(list(lista2))
