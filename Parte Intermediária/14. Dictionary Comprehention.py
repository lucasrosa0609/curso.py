"""
l1 = [1,2,3,4,5,6]
l2 = [v*2 for v in l1]
print(l2)
"""

lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2')
]

d1 = {f'chave_{x}': x**2 for x in range(5)}  # chave para dicionarios, poderia ter usado dict
# print(d1, type (d1))  # pode usar compreensao de conjuntos (sets)
print(d1)
