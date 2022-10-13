from functools import reduce
from dados import *

soma_idades = reduce(lambda acumulador, pessoa: acumulador + pessoa['idade'], pessoas, 0)
print(soma_idades / len(pessoas))
