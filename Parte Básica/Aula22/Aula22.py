'''
For in em python
iterando strrings com for
função range(start=0, stop, step=1)
'''
# cont = 0
# texto = 'Python'
'''
while cont < len(texto):
    print(texto[cont])
    cont += 1
'''
'''
# enumerate
for i, letra in enumerate(texto):
    print(i, letra)

'''
'''
for n in range(10):  # (começa no 0 ou no número definido, pula essa qtde de numeros, termina nesse número)
    print(n)

for n in range (100):
    if n % 8 == 0:
        print(n)

'''

texto = 'Python'
nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string += letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra

print(nova_string)