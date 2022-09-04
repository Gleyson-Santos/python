"""
Listas em python
fatiamento
append, insert, pop, del, clear, extend + range
"""
chance = 6
secreto = 'perfume'
digitadas = []
end_of_game = True
while end_of_game:
    if chance <= 0:
        print('Você perdeu!!!')
        end_of_game = False

    letra = input('Digite uma letra\n')
    if len(letra) > 1:
        print('Digite apena uma letra')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'Que legal, a letra {letra} existe na palavra secreta.')
    else:
        print(f'a letra {letra} não existe na palavra secreta.')
        print(f'{chance}')
        digitadas.pop()

    temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            temporario += letra_secreta
        else:
            temporario += '*'

    if temporario == secreto:
        print(f'Que legal, você ganhou. A palavra secreta era {secreto}')
        end_of_game = False
    else:
        print(f"A palavra secreta era {temporario}")

    if letra not in secreto:
        chance -= 1

    print(f'Você ainda tem {chance} chances.')
    print()
