'''
Operadores lógicos:
and, or, not
in e not in
'''

# comparacao1 and comparacao2 - vai checar se a comparação 1 é verdadeira E a comparação 2 é verdadeira = true/false
# se uma das duas comparações for falsa, vai retornar false

# comp1 or comp2 - a comp1 é verdadeira OU a comp2 é verdadeira, se uma das duas for, o resultado vai ser true

'''
a = 2
b = 3
if b>a:
    print ('B é maior que A')
else:
    print('A é maior que B')


if not b>a:
    print ('B é maior que A')
else:
    print('A é maior que B')  # usado com variáveis vazias


# if not a:      usado pra caso o valor de A fosse 0 ou não houvesse nada
    # print ('Por favor preenhca o valor de A')

nome = input('Qual seu nome ai o seu esquisito do caraio? ')

if 'asdas' in nome:
    print ('Por favor escolha outro nome')
else:
    print ('Parabéns, seu nome é elegível')
'''

usuario = input('Nome de usuário: ')
senha = input('Senha: ')

usuario_bd = 'lucas'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logando')
else:
    print('Usuário ou Senha inválidos')
