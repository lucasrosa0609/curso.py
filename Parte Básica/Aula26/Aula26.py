'''
Split, Join, Enumerate
- Split - Dividir uma string # str
- Join - Juntar uma lista # str
- Enumerate - Enumerar elementos da lista # list / para objetos iteráveis
'''
'''
string = 'A marina é uma gatona, mas não consegue entender isso isso isso isso'
list = string.split(' ')
palavra = ''
count = 0
lista2 = string.split(',')
'''
'''
for valor in list:
    print(f'A palavra *{valor}* apareceu {list2.count(valor)} vezes')
'''
'''for valor in lista2:
    print(valor.strip().capitalize())
for valor in list:
    qtd_x = list.count(valor)
    if qtd_x > count:
        count = qtd_x
        palavra = valor
        print(f'A palavra que apareceu mais vezes foi *{palavra}*, que apareceu {count} vezes')
'''

'''ex = 'O brasil é penta'
list = ex.split()
list.append([1, 2] + [5, 6])'''

list = [
    [1,2],
    [3,4],
    [4,5],

]

for v in list:
    print (v[0], v[1])
