# lists, tuples, str -> Sequences -> Iteraveis
# for converte nome em iterador usando o next, quando chega no fim, se ele chamar de novo o next, vai criar uma excecao
nome = 'Lucas Rosa'
iterador = iter(nome)
gerador = (letra for letra in nome)
"""
try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
except:
    pass


print("Cade os valores")
for valor in iterador:
    print(valor)
    """
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

for letra in gerador:
    print(letra)
"""
for letra in nome:
    print(letra)

print('#' * 80)

for letra in nome:
    print(letra)

print(nome)
"""

