
# nome = input('Qual o seu nome? ')
'''
if nome:
    print(nome)
else:
    print('Não digitou nada')
'''
'''print(nome or 'Você não digitou nada')

print(nome or None or False or 0 or 'Você não digitou nada')
'''
a = 0
b = None
c = False
d = []
e = {}
f = 22
g = 'Lucas'

variavel = a or b or c or d or e or f or g
print(variavel)

