
class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def gera_id():
        from random import randint
        # rand = randint(10000, 19999)
        return randint(10000, 19999)


p1 = Pessoa('Gleyson', 36)
print(p1.por_ano_nascimento('Gleyson', 36))
print(Pessoa.gera_id())
