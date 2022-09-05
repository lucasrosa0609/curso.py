def converte_numero(valor):
    return float(valor)


while True:
    try:
        numero = converte_numero(input('Digite um numero: '))
        print(numero * 5)
    except ValueError as error:
        print('Por favor, digite apenas numeros')

