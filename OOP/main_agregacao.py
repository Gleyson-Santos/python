from agregacao import Produtos, CarrinhoDeCompras

carrinho = CarrinhoDeCompras()

p1 = Produtos('Camiseta', 50)
p2 = Produtos('iPhone', 10000)
p3 = Produtos('Caneca', 15)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p3)
carrinho.inserir_produtos(p3)
print(carrinho.produtos)
print(carrinho.soma_total())
