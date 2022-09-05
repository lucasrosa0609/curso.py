# import math
#
# PI = math.pi
#
#
# def dobra_lista(lista):
#     return [x*2 for x in lista]
#
# def multiplica(lista):
#     r = 1
#     for i in lista:
#         r *= i
#     return r
#
#
# # lista = [1, 2, 3, 4, 5]
#
# print(dobra_lista(lista))
# print(multiplica(lista))
#
# import calculos
#
# print(calculos.PI)
#
# lista = [2,4]
# print(calculos.multiplica(lista))

from calculos import multiplica, dobra_lista
from outro import fala_oi

lista = [375, 345]

print(multiplica(lista))
fala_oi()