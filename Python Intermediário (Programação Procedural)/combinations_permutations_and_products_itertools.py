"""
Combinations, permutations e product - itertools
Combinação - Ordem não importa
Permutação - Ordem não importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = [nome.title() for nome in ['luiz', 'andré', 'eduardo', 'leticia', 'fabricio', 'rose']]

for grupo in product(pessoas, repeat=2):
    print(grupo)
