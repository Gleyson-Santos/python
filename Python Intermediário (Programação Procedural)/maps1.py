from dados import *

nova_lista = map(lambda item: item * 2, lista)
new_list = [item * 2 for item in lista]
print(lista)
print(new_list)
print(list(nova_lista))
