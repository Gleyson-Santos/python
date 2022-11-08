class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nome_clase = self.__class__.__name__

    def falar(self):
        print(f'{self.nome_clase} esta falando ...')


class Cliente(Pessoa):
    def comprar(self):
        print(f'{self.nome_clase} esta comprando ...')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome_clase} esta estudando ...')
