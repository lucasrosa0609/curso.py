# criar um pacote, python package

from vendas import calc_preco


preco = 49.90
preco_com_aumento = calc_preco.aumento(valor=preco, porcentagem = 15)
print(preco_com_aumento)

preco_com_reducao = calc_preco.reducao(valor=preco, porcentagem = 15)
print(preco_com_reducao)