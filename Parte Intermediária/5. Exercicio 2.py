'''
1- Crie uma função1 que recebe uma função22 como parâmetro e retorne o valor da função 2 executada
'''
'''
v = 'via tomar no cu'

def ola_mundo():
    return v

def mestre(func):
    return func()

executando = mestre(ola_mundo)

print(executando)
'''


'''
2- Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor da função2 executada. Faça a função1 execu
tar duas funções que recebam um número diferente de argumentos
'''


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def f1(nome):
    return f'Oi, {nome}'

def f2(nome, saudacao):
    return f'{saudacao} {nome}'


ex1 = mestre(f1, 'Lucas')

ex2 = mestre(f2, 'Lucas', saudacao='Bom dia!')

print(ex1)
print(ex2)

