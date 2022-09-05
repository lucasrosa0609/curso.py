"""
zip - unindo iteraveis
zip_longest - Itertools
"""

from itertools import zip_longest, count

indice = count()
cidades = ['Sao Paulo', 'Belo Horizonte', 'Salvador', 'Rio de Janeiro']
estados = ['SP', 'MG', 'BA']

cid_est = zip(cidades, estados)
cid_est1 = zip_longest(
    indice,
    cidades,
    estados,
    fillvalue='Estado'
)
cid_est2 = zip(
    indice,
    cidades,
    estados,
)

"""
for v in cid_est:
    print(v[0], v[1])
"""

print(list(cid_est2))

for indice, cidade, estado in cid_est2:
    print(indice, cidade, estado)

