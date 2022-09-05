# try:
#     a = {}
#     print(a[1])
# except NameError as erro:
#     print('Erro:', erro)
# except (IndexError, KeyError) as erro:
#     print('Indice inexistente')
# except Exception as erro:
#     print('Ocorreu um erro inesperado')
# else:
#     pass
#
# print()
# print('Pipipipopopo...')

try:
    a = 1/0
except NameError as erro:
    print('Erro:', erro)
except (IndexError, KeyError) as erro:
    print('Indice inexistente')
except Exception as erro:
    print('Ocorreu um erro inesperado')
else:
    print('Seu codigo foi executado com sucesso')
finally:  # ocorreu ou nao um erro, ela vai ser executada. Serve pra finalizar um arquivo ou etc
    a = 'None'
    print(a)
