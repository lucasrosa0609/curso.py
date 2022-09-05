"""
Combination, Permutations e Product - Itertools
Combinations - Ordem n'ao importa
Permutations - Ordem importa
Ambos nao repetem valores unicos
Produto - Ordem importa e repete valores
"""
from itertools import combinations, permutations, product
pessoa = ['Lucas', 'Marina', 'Ana', 'Leticia', 'Joao', 'Rodrigo']

for grupo in combinations(pessoa, 2):
    print(grupo)



for grupo in permutations(pessoa, 2):
    print(grupo)

print('#' * 80)

for grupo in product(pessoa, repeat=2):  # produt precisa de repeat, as outras nao
    print(grupo)

print('#' * 80)

for grupo in combinations(pessoa, 3):
    print(grupo)
