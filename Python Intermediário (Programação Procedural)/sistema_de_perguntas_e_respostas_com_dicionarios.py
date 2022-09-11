perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2? ',
        'reposta': {'a': '1', 'b': '4', 'c': '5', },
        'reposta_certa': 'b', },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 + 2? ',
        'reposta': {'a': '1', 'b': '4', 'c': '5', },
        'reposta_certa': 'c', }, }
resposta_certa = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')
    print('Escolha uma das opções abaixo: ')
    for rk, rv in pv['reposta'].items():
        print(f'[{rk}]: {rv}')

    reposta_usuario = input('Sua resposta: ')
    if reposta_usuario == pv['reposta_certa']:
        print('Acertou')
        resposta_certa += 1
    else:
        print('Você errou!!! ')
