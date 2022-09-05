""""
Modulos padrao do python:
Modulos sao arquivos .py (que cntem codigo python) e servem para expandir as funcionalidades
padroes da linguagem
Veja todos os modulos padrao do python em: https://docs.python.org/3/py-modindex.html
"""
# import sys
# print(sys.platform)

from sys import platform as pl
from random import randint as qualquerapelido

print(pl)
print()


from random import randint as qualquerapelido


def randint(*args):
    return 'hahaha'


print(qualquerapelido(1, 25))
print()

for i in range(5):
    print(qualquerapelido(1, 25))


def randint(*args):
    return 'hahaha'

# from random import * -> isso importa tudo do modulo, so que fica muito mais complexo saber
# from random, import randit, random

import pymysql

