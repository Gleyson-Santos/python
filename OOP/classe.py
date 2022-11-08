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

    def falar(self):
        print('Estou em cliente')


class ClienteVip(Cliente):
    def __init__(self, nome, idade, sobrenome):
        Pessoa.__init__(self, nome, idade)
        self.sobrenome = sobrenome

    def falar(self):
        Pessoa.falar(self)
        Cliente.falar(self)
        print('Cliente vip esta falando')


class Aluno(Pessoa):
    def estudar(self):
        print(f'{self.nome_clase} esta estudando ...')
