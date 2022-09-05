'''
while/else
Contadores
Acumuladores
'''

contador = 257
acumulador = 0
c = contador
a = acumulador
c = c + 77
a = a + c


while c <= 4600:
    print(c, a)
    c = c + 77
    print(min(c))


else:
    print(f'{c} atingiu o número maior do que 10')

