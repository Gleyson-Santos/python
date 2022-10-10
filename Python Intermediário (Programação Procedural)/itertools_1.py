"""
count - itertools
"""

from itertools import count

contador = count(start=50, step=-2)
for valor in contador:
    print(valor)
    if valor < 0:
        break
