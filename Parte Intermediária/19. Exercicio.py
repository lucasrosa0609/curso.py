"""
Considerando duas listas de inteiros ou floats (lista a e lista b), some os valores nas listas retornando uma nova lista
com os valores somados:

Se uma lista for maior que a outra, a soma so vai considerar o tamanho da menor

Exemplo:
lista_a = [1,2,3,4,6,7]
lista_b = [1, 2, 3, 4]
===================== resultado
lista_soma = [2, 4, 6, 8]
"""

lista_a = [1, 2, 3, 4, 6, 7]
lista_b = [1, 2, 3, 4]
# minha solucao:
"""
soma = zip(lista_a, lista_b)
soma1 = [(x + y) for x, y in soma]
print(soma1)
"""
# solucao aula:
lista_soma = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma)
