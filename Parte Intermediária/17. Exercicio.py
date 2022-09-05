# Carrinho vazio e é adicionado produtos conforme o cliente adiciona produtos nele
# Não são produtos simples, que tem variações em base de dados

carrinho = []
carrinho.append(('Produto', 20.99))
carrinho.append(('Produto2', 30))
carrinho.append(('Produto3', 50))
carrinho = iter(carrinho)
"""
for v, v1 in carrinho:
    print(type(v1))
"""

"""
lc_carrinho = [v[1] for v in carrinho]
print(lc_carrinho)
"""


"""
lc = [x for x in carrinho]
lc += lc
print(lc)
"""
# somar o preco total do carrinho com list comprehention

# Liquidificadores com variações, 110w, 220w, etc

# solucao

#resposta

total = sum([float(y) for x,y in carrinho])
print(carrinho)
print(total)