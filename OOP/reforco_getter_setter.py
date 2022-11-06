# setter configurando um valor
# getter obter um valor

class Pessoa:

    def __init__(self):
        self.attr = 'atributo'

    @property
    def nome(self):
        return 'Gleyson'

    @nome.setter
    def nome(self, nome):
        self.attr = nome
