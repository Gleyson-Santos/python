from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Leticia', 'nota': 'B'},
    {'nome': 'Fabricio', 'nota': 'C'},
    {'nome': 'Rosemary', 'nota': 'D'},
    {'nome': 'Joana', 'nota': 'E'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'R'},
    {'nome': 'André', 'nota': 'S'},
    {'nome': 'Anderson', 'nota': 'T'},
    {'nome': 'José', 'nota': 'Z'}

]
ordena = lambda item: item['nota']
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)
for agrupamento, valores_agrupados in alunos_agrupados:
    print(f'Agrupamento: {agrupamento}')
    for valor in valores_agrupados:
        print(valor)
