from dados import produtos, pessoas, lista

# lista_filtro = filter(lambda x: x > 5, lista)
#
#
# nova_lista = [x for x in lista if x > 5]
#
#
# print(nova_lista)
# print(list(lista_filtro))

# def filtra(produto):
#     if produto ['preco'] > 50:
#         return True


def filtra1(p):
    if p['idade'] < 18:
        return True


idade = filter(filtra1, pessoas)

for i in idade:
    print(i)




# produtos_maiores = filter(lambda p: p['preco'] > 50, produtos)
#
# produtos_maiores1 = filter(filtra, produtos)
#
# for produto in produtos_maiores:
#     print(produto)
# print()
# for produto in produtos_maiores1:
#     print(produto)
