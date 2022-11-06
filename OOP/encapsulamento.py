"""
public, private, protected
_ public/private
__ protected (mangling name python)
"""


class BaseDeDados:

    def __init__(self):
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir(self, idx, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {idx: nome}
        else:
            self.__dados['clientes'].update({idx: nome})

    def lista(self):
        for idx, nome in self.__dados['clientes'].items():
            print(idx, nome)

    def apaga(self, valor):
        del self.__dados['clientes'][valor]


bd = BaseDeDados()
bd.inserir(1, 'Gleyson')
bd.__dados = 'outra coisa'
bd.inserir(2, 'Andre')
print(bd.dados)
