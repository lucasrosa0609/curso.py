'''
While
'''
'''
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = frase[contador]
# print(f'{frase} tem o tamanho de {tamanho_frase} caracteres')

while contador < tamanho_frase:
    # print(frase[contador], contador)
    nova_string += frase[contador]
    print(f'{nova_string} vai somar uma letra de cada vez no texto')
    contador += 1
'''

contador = 0
frase = 'O meu nome é Lucas de Souza Fernandes Rosa'
tamanho_frase = len(frase)
nova_string = ''

in_us = input('Qual letra deseja colocar maíuscula: ')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == in_us:
       nova_string += in_us.upper()
    else:
        nova_string += letra
    contador += 1

print(nova_string)







