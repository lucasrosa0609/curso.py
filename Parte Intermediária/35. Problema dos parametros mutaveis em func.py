# mutaveis = [], {}
# imutaveis = tuplas, strings, numeros, booleanos, none

def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista

clientes1 = lista_de_clientes(['Joao', 'Maria', 'Eduardo'])
clientes2 = lista_de_clientes(['Marcos', 'Jonas', 'Zico'])


print(clientes1)
print(clientes2)

