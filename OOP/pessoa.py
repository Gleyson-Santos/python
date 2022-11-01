class Pessoa:

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto='Assunto'):
        if self.comendo:
            print('Não pode falar comendo ...')
            return

        print(f'{self.nome} esta falando sobre {assunto}')

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já esta comendo')
            return

        print(f'{self.nome} esta comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não esta comendo')
            return
        self.comendo = False
