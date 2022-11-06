class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))


    # getter
    @property
    def nome(self):
        return self._nome

     # setter
    @nome.setter
    def nome(self, valor):
        self._nome = valor.upper()

    # getter
    @property
    def preco(self):
        return self._preco

    # setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

p1 = Produto('camiseta', 150)
p1.desconto(10)
print(p1.nome)
print(p1.preco)

p2 = Produto('calça', 'R$250')
p2.desconto(17)
print(p2.nome)
print(p2.preco)
