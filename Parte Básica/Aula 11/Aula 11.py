'''
Operadores relacionais
==; >; >=; <; <=;
!=  - DIFERENTE
'''

'''
print(2 == 1)  # valor vai ser false, porque 2 não é igual a 1
print(2 == '2')  # valor vai ser false, porque str não é int
'''

'''
num_1 = 2
num_2 = 3

expressao = (num_1 != num_2)

print(expressao)


var_1 = 'Lucas'
var_2 = 'Rosa'

expressao_1 = (var_1 != var_2)

print(expressao_1)
'''

nome = input('Qual seu nome? ')
idade = int(input('Qual sua idade? '))

#Limite empréstimo
menor_20 = 20
acima_30 = 30

if idade >= menor_20 and idade <= acima_30:
    print(f'{nome} pode pegar o empréstimo')
else:
    print (f'{nome} não está permitido a fazer o empréstimo')

