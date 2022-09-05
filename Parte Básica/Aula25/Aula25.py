'''
for/else em python
'''

variavel = ['Lucas Rosa', 'Rodrigo', 'Gabriel']
cmccl = False

for valor in variavel:
    if valor.startswith('L'):
        cmccl = True
        if cmccl:
            print(valor)
            pass
        else:
            print('Ngm começa com L')

'''
variável = input('Digite um texto aqui: ')
variável_u = list(variável.split(', '))
cmccl = False
remover = 'L'

print('variável:', variável_u)
for valor in variável_u:
    if valor.startswith('L'):
        if cmccl:
            print(variável_u)
        else:
            print('Ngm começa com L')
'''
