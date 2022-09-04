"""
Split, join, enumerate em Python
* split - Dividir uma string #str
* join - Juntar uma string #str
* enumerate - Enumerar eçementos da lista #list
"""
lista = [
    ['edu', 'joão', 'luiz'],
    ['maria', 'aline', 'joana'],
    ['helena', 'ed', 'lu', [
        'carlos', 'valdir', 'anderson'
    ]],
]

enumerada = enumerate(lista, 50)
for v1, v2 in enumerada:
    print(v1, v2)
