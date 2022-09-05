'''
lambda pode ser uma função anônima
'''
'''
a = lambda x, y: x * y

print(a(2,2))
'''
#  quando precisa passar função por parâmetro pra outra função, ou outro método
#  exemplo:

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

print(sorted(lista, key=lambda i: i[0], reverse=True))


'''
def func(item):  # key=lambda item: item[1] -> é a MESMA COISA!!!!!
    return item[1]  # 


lista.sort(key=func, reverse=True)
print(lista)
'''