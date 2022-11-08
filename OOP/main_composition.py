from composition import Endereco, Cliente

cliente1 = Cliente('Luiz', 32)
cliente1.inserir_enderecos('Belo Horizonte', 'MG')
cliente1.lista_enderecos()
del cliente1

# print(50 * '*')

cliente2 = Cliente('Maria', 19)
cliente2.inserir_enderecos('São Paulo', 'SP')
cliente2.inserir_enderecos('Salvador', 'BA')
cliente2.lista_enderecos()
del cliente2

print(50 * '*')
