"""
# o que e um iteravel

lista = [0,1,2,3,4,5]  # objeto iteravel
print(hasattr(lista, '__iter__'))  # confirmar se e iteravel

for v in lista:   # for transforma nossa lista em um iterador
    print(v)

lista = iter(lista)
print(hasattr(lista, '__next__'))

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))

# lista e iteravel mas nao necessariamente um iterador, um iterador vai dar um valor de cada vez
"""
# geradores normalmente sao utilizados qdo precisamos usar valores que usam mta memoria, ou mto tempo

import sys
import time
"""
lista = list(range(10))
print(sys.getsizeof(lista))  # otimizacao de codigo n e interessante salvar a lista na memoria, geradores servem p isso
"""

"""
def gera():
    r = []
    for n in range(100):
        yield n
        time.sleep(0.1)
    return r
"""
"""
def gera():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel

g = gera()

for v in g:
    v = v + 1 
    print(v)

"""
"""
lista = [x for x in range(1000)]
print(type(lista))
lista = (x for x in range(1000))  # nao ha necessidade de criar funcao pra criar gerador, basta colocar parentesis
print(type(lista))
print(sys.getsizeof(lista))
"""

l1 = [x for x in range(10000)]
l2 = (x for x in range(10000))

print(sys.getsizeof(l1))  # aumenta conforme o tamanho porque salva todos os valores na memoria
print(sys.getsizeof(l2))  # gerador sempre usa os mesmos valores de memoria

for v in l2:
    print(v)


