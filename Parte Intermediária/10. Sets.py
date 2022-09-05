# add (adiciona
# update (atualiza)
# clear
# discard
# union | (une)
# intersection & (todos os elementos presentes nos dois sets)
# differente - (elementos apenas no set da esquerda)
# symmetric_differente ^ (Elementos que estao nos dois sets, mas nao em ambos)
# sets nao respeitam ordem
# nao aceitam elementos duplicados
# utilizado geralmente pra eliminar elementos duplicados de uma lista
'''
s1 = {1, 2, 3, 4, 5}  # pra criar set vazio o certo e set()
s1.add(25)
s1.add(23)
s1.discard(2)
s1.update('Python')  # iteravel e recebe iteracoes


for v in s1:
    print(v)
'''
'''
lista_1 = [1,2,3,4,5,5,5,5,5,5,6,7,67,6,6,5,4,3,1,2,34,5,6,1,2,3,4,154, 'Lucas', 'Lucas']
lista_1 = set(lista_1)
lista_1 = list(lista_1)


print(lista_1)
'''
'''
s1 = {1, 2, 3, 4, 5, 7}
s2 = {1, 2, 3, 4, 5, 6}

s3 = s1 & s2
s4 = s1 - s2
s5 = s2 ^ s1

print(s3)
print(s4)
print(s5)
'''

l1 = ['Luiz', 'Maria', 'Lucas']
l2 = ['Maria', 'Lucas', 'Luiz', 'Luiz', 'Luiz','Lucas', 'Lucas']

if set(l1) == set(l2):
    print('L1 = L2')
else:
    print('L1 =/= L2')