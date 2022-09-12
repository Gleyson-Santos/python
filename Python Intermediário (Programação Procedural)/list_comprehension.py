"""
List Comprehension
"""
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = ['Luiz', 'Mauro', 'Maria']
l3 = list(range(100))

ex1 = [variavel for variavel in l1]
ex2 = [v*2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]
ex4 = [v.upper() for v in l2]

tupla = (
    ('chave um', 'valor dois'),
    ('chave2', 'valor2'),
)
ex5 = [(x, y) for y, x in tupla]
ex5 = dict(ex5)
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
ex7 = [v if v % 3 == 0 else f'{v} Não é divisivel ' for v in l3]

print(ex7)
