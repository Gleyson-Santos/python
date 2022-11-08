class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_enderecos(self, cidade, estados):
        self.enderecos.append(Endereco(cidade, estados))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(self.nome)
            print(endereco.cidade)
            print(endereco.estado)

    def __del__(self):
        print(f'{self.nome} foi apagado')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.cidade} foi apagado')
        print(f'{self.estado} foi apagado')
