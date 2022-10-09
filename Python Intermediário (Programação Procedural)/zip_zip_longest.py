"""
zip - unindo iteraveis
zip_longest - itertools
"""
from itertools import zip_longest, count
indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']
estados = ['SP', 'MG', 'BA']

cidade_estados = zip(indice, cidades, estados)
for indice, cidades, estados in cidade_estados:
    print(indice, cidades, estados)
