'''
Crie uma função que exibe uma saudação com os parâmetros saudação e nome
'''


def func(saudacao = input('Qual saudação você prefere? '),
         nome = input('Qual seu nome? ')):
    print(saudacao, nome)
    return saudacao, nome


var = func()
print(var)

'''
Crie uma função que recebe 3 números como parâmetros e exiba a soma entre eles
'''


def func1(n1 = input('Um número: '),
          n2 = input('Outro número: '),
          n3 = input('Mais um número: ')):
    n1, n2, n3 = int(n1), int(n2), int(n3)
    return n1 + n2 + n3


var1 = func1()
print(var1)


'''Crie uma função que receba 2 numeros. O primeiro é um valor e o segundo é um percentual. Retorne o valor do primeiro
número somado do aumento do percentual do mesmo.
'''


def func2(v1=input('Defina um valor: '),
          v2=input('Preencha com um percentual: ')):
    v1 = float(v1)
    v2 = float(v2)
    return v1 + (v1*(v2/100))


var2 = func2()
print(var2)

'''
Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz, se o parâmetro da função dor divisível por 5,
retorne buzz. Se o parâmetro for divisível por 5 e por 3, retorne fizzbuzz, caso contrário, retorne o número enviado.
'''


def func3(v1=input('Escolha um número: ')):
    v1 = int(v1)
    if v1 % 3 == 0 and v1 % 5 == 0:
        return 'FizzBuzz'
    if v1 % 5 == 0:
        return 'Buzz'
    if v1 % 3 == 0:
        return 'Fizz'
    return True


var3 = func3()
print(var3)







