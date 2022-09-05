'''
Funções - def em Python (pt.1)
'''

usuario = input('Como você gostaria de ser chamado? ')

def funcao(msg='Olá', nome= usuario):
    print(msg, nome)
    nome = nome.replace ('e', '3')
    msg = msg.replace ('e', '3')
    return f'{msg} {nome}'


variavel = funcao()

print(variavel)

'''
def funcao(var):
    print('Isso não será executavo')
    return var  # não passa do valor return, tudo chega apenas até a função return
    


variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor')
'''

'''
def divisao(n1, n2):
    if n2 or n1 == 0:
        return  # se return for utilizado aqui, e n1 ou n2 for 0, ele sequer continua e pula direto pro ''else''

    return n1/n2


divide = divisao(8,2)

if divide:
    print(divide)
else:
    print('Conta inválida')
'''

'''
def dumb():
    return [1, 2, 3, 4, 5, 6]  # pode retornar qualquer coisa, inclusive nada, que será none


variavel = dumb()
print(variavel, type(dumb()))

'''

'''
def f(var):
    print(var)


def dumb():
    return f


var = dumb()
print(id(var), id(f))

if var == f:
    print('É igual')
else:
    print('Não é igual')
'''

'''
def dumb():
    return ('Luiz', 'Otávio')
var = dumb()

print(var, type(var))  # tupla é uma variável que não pode ser alterada
'''
