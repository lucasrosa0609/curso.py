'''
Listas em python
fatiamento
apprend, insert, pop, del, clear, extend, +
min, max
range
'''

# bool = true/false
# inteiros = 10
# flutuante = 10.10
# strings = 'Textos'
'''
texto = valor
lista = [1, 2, 3, 4, 'Lucas Rosa', True, 10.5]  # aceita várias possibiolidades
'''
'''
#índices = 0    1    2    3    4
lista =  ['A', 'B', 'C', 'D', 'E']
#         -5   -4   -3   -2   -1

print(lista[0:3:2])  # começa do 0: vai até o 3 sem exibir o 3: pula de 2 em 2 casas)
print(lista[::-1])
'''
'''
l1 = [1,2,3]

l2 = [4,5,6]
print(l2)

# l3 = l1+l2  # concatenando, não é soma

# l1.extend(l2)  # l1 passa a ter o valor de l1 e l2
# l1.extend('a')  # passa a ter um valor a mais, 'a'
# l1.append('a')  # mais comumente usado
#l2.append('b')  # insere um novo valor no final da lista

l2.insert(0, 'banana')  # insert(indice, valor a ser inserido)
print(l2)
l2.pop(3)  # remove um valor da lista
print(l2)
'''
'''
l2 = [1,2,3,4,5,6,7,8,9]
print(l2)
l2.insert(0, 'banana')
print(l2)
del(l2[0])
print(l2)
'''
'''
l2 = list(range(1, 10))
# print(l2)

soma = 0
for valor in l2:
    soma = soma + valor
    print(soma)
    '''
'''
l2 = ['String', True, 10, -20.5]

for elem in l2:
    print(f'O tipo é {type(elem)} e o seu valor é {elem}')
'''

secreto = 'o gabriel come merda'
digitadas = []
chances = 4
while True:
    if chances <= 0:
        print('Você é muito burro, infelizmente')
        break
    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Ah não, pô, digita uma letra só')
        continue

    elif letra in secreto:
        digitadas.append(letra)
        print('Você está quase lá')
        print(digitadas)

    if letra in secreto:
        print('Você acertou')

    if letra not in secreto:
        chances -= 1
        print('Sua letra não vale pro joguinho')
        print(f'Você tem mais {chances} chances')
        continue

    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += ' '
    print(secreto_temp)

