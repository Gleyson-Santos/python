from vendas import calc_price


preco1 = 10.00

preco_com_aumento = calc_price.aumento(preco1, 10)
preco_com_reducao = calc_price.reduz(preco1, 10)
print(preco_com_aumento)
print(preco_com_reducao)
