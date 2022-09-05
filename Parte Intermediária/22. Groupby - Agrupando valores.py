from itertools import groupby, tee  # tee faz copia dos iteradores em variaveis
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Lucas', 'nota': 'B'},
    {'nome': 'Marina', 'nota': 'C'},
    {'nome': 'Marina', 'nota': 'C'},
    {'nome': 'Marina', 'nota': 'C'},
    {'nome': 'Ana', 'nota': 'D'},
    {'nome': 'Rodrigo', 'nota': 'A'},
    {'nome': 'Rodrigo', 'nota': 'A'},
    {'nome': 'Rodrigo', 'nota': 'A'},
    {'nome': 'Rodrigo', 'nota': 'A'},
    {'nome': 'Rodrigo', 'nota': 'A'},
    {'nome': 'Rodrigo', 'nota': 'A'},
    {'nome': 'Lenina', 'nota': 'B'},
    {'nome': 'Eduardo', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'A'},
    {'nome': 'Maria', 'nota': 'C'},
    {'nome': 'Maria', 'nota': 'C'},
    {'nome': 'Maria', 'nota': 'C'},
    {'nome': 'Jose', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'D'},
]

ordena = lambda item: item['nota']
print(ordena)
alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)  # tem que repetir o codigo

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)

    print(f'Agrupamento: {agrupamento}')

    quantidade = len(list(va1))

    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()

    for aluno in va2:
        print(f'\t{aluno}')

