'''
Documentação
'''
import re

'''
num1 = input('digite um número: ')
num2 = input('digite outro número: ')

# isnumeric; isdigit; isdecimal
# números e positivos (123456), com . essas funções não funcionarão

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)
    print(num1+num2)
else:
    print('Não pude converter os números pra realizar as contas, favor utilizar apenas números')
'''

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('Erro')


