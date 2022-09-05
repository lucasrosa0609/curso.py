from dados import produtos, pessoas, lista
from functools import reduce

# acumula = 0
#
# for item in lista:
#     acumula += item
#
# print(acumula)

soma_lista = reduce(lambda ac, i: i['preco'] + ac, produtos, 0)
print(soma_lista/len(produtos))
print()
soma_idade_pessoas = reduce(lambda ac, ps: ps['idade'] + ac, pessoas, 0)
for pessoa in pessoas:
    print(pessoa)
print()
print(soma_idade_pessoas)
print()
print(soma_idade_pessoas/len(pessoas))
