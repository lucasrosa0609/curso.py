# vao envolver as funcoes que eu quiser, mudando ou nao o comportamento


# def fala_oi():
#     print('Oi')
#
#
# fala_oi()
#
#
# variavel = fala_oi
# variavel()
#
# print(type(variavel))

# def master(funcao):
#     def slave(*args,**kwargs):
#         print('Decoradasso')
#         funcao(*args,**kwargs)
#     return slave
#
# @master
# def fala_oi():
#     print('Oi')
#
# @master
# def outra_funcao(msg):
#     print(msg)
#
# fala_oi = master(fala_oi)
# fala_oi()
#
# outra_funcao('Ola, eu sou o Lucas')

from time import time
from time import sleep


def velocidade(func):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = func(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f'\nA funcao {func.__name__} levou {tempo:.2f}ms para executar.')
        return resultado
    return interna()

@velocidade
def demora():
    for i in range(1000):
        print(i, end='')


# demora()
