nomes = ['Luiz', 'Maria', 'Helena', 'Joana', 'Felipe']

novos_nomes = [
    nome[:-1:].upper() + nome[-1].lower()
    for nome in nomes

]

print(novos_nomes)
