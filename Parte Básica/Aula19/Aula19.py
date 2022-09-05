'''
Repetição
utilizado para realizar ações ENQUANTO uma condição for verdadeira

requisitos: entender condições e operadores
'''
'''
num1 = int(input('Qual a sua idade? '))

while num1 > 18:
    nome = input('Qual o seu nome? ')
    print(f'Olá, {nome}')
'''
'''
x = 0

while x < 10:
    if x == 3:  # vai pular o 3
        x = x + 1  # isso aqui tem q estar ANTES do continue
        break  # aqui vai acabar
        continue
    if x == 5:
        x = x + 1
        continue
    print(x)
    x = x + 1
print('acabou')
'''
'''
x = 0  # coluna

while x < 10:
    y = 0
    while y < 5:
        print(f'{x},{y}')
        y += 1
    x += 1


print('Acabou')
'''

login = input('Login: ')
login_db = 'lusofero@gmail.com'
senha = input('Senha: ')
senha_db = '123456'

if login != login_db or senha != senha_db:
    print ('Usuário ou senha incorretos. Tente novamente')

while login == login_db and senha == senha_db:
    num1 = input('Digite um número: ')
    if not num1.isnumeric():
        print(f'{num1} não é um número, favor digitar apenas números')
        continue
    num2 = input('Digite outro número: ')
    if not num2.isnumeric():
        print (f'{num2} não é um número, favor digitar apenas números')
        continue
    operador = input('Digite um operador: ')
    num1 = int(num1)
    num2 = int(num2)
    # +, -, /, *
    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '*' or operador == 'x':
        print(num1 * num2)
    elif operador == '/':
        print(num1 / num2)
    elif operador != ('+', '-', '*', 'x', '/'):
        print ('Operador inválido')
