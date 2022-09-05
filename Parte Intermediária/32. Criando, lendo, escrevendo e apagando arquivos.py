# https://docs.python.org/3/library/functions.html#open
#
# try:
#     file = open('abc.txt', 'w+')  # w+ = leitura e escrita
#     # file.write('Linha 1\n')
#     # file.write('Linha 2\n')
#     # file.write('Linha 3\n')
#     #
#     # file.seek(0, 0)  # normalmente usa o 0 mesmo
#     # print('Lendo linhas:')
#     # print(file.read())
#     # print('###########')
#     #
#     # file.seek(0, 0)
#     # print(file.readline(), end='')  # vem p final da linha e se usar dnv ele comeca de ond parou
#     # print(file.readline(), end='')  # vem p final da linha e se usar dnv ele comeca de ond parou
#     # print(file.readline(), end='')  # vem p final da linha e se usar dnv ele comeca de ond parou
#     # print('###########')
#     # file.seek(0, 0)
#     # # print(file.readlines())  # p/ corrigir, usar laco for
#     #
#     # for linha in file.readlines():
#     #     print(linha, end='')
#     file.write('Linha')
#     file.seek(0, 0)
#     print(file.read())
# finally:
#     file.close()
#

# with open('abc.txt', 'w+') as file:  # nao e necessário mandar fechar o arquivo com
#     file.write('Linha 1\n')          # file.close()
#     file.write('Linha 2\n')
#     file.write('Linha 3\n')
#
#     file.seek(0)
#     print(file.read())
#
#
# with open('abc.txt', 'r') as file:  # apenas lendo o arquivo
#     print(file.read())


# with open('abc.txt', 'a+') as file:  # coloca o cursor no final do arquivo
#     file.write('Outra linha')
#     file.seek(0)
#     print(file.read())

# para remover arquivo basta fazer import os e dar o comando os.remove 'abc.txt'


import json

d1 = {
    'Pessoa 1': {
        'Nome': 'Luiz',
        'Idade': 25
    },
    'Pessoa 2': {
        'Nome': 'Rose',
        'Idade': 30
    },
}

d1_json = json.dumps(d1, indent=True)

with open('abc.json', 'w+') as file:
    file.write(d1_json)
    
print(d1_json)
