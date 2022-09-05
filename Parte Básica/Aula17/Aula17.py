'''
Formatação de valores com modificadores

:s - Texto
:d - INteiros
:f - Números de ponto flutuante
:.(Número)f-  Qtde de casas decimais
:(Caractere) (> ou < ou ^) (QUANTIDADE) (TIPO - s, d ou f)
'''

'''
num_1 = 10
num_2 = 3
divisão = num_1 / num_2
print(f'{divisão:.2f}')

nome = 'Lucas Rosa'
print(f'{nome:s}')

num_1 = 1
print(f'{num_1:0>10}')

num_2 = 1150
print (f'{num_2:0>10}')

num_3 = 13024
print (f'{num_3:0^10}')

num_4 = 1250
print (f'{num_4:0^10.2f}')

nome = 'Lucas'
sobrenome = 'Rosa'
nome_format = '{0:$^50} {1:#^50}'.format(nome, sobrenome)
print(nome_format)
'''

nome = 'Lucas Rosa'
nome = nome.lower()
print(nome.islower())