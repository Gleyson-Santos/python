perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2? ',
        'reposta': {'a': '1', 'b': '4', 'c': '5', },
        'reposta_certa': 'b', },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 + 2? ',
        'reposta': {'a': '1', 'b': '4', 'c': '5', },
        'reposta_certa': 'C', }, }

for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Escolha uma das opções abaixo: ')
    for rk, rv in pv['reposta'].items():
        print(f'[{rk}]: {rv}')
