'''
semelhantes com listas
'''
'''
d1 = {1:'valor', 2:'valor', 3:'valor'}  # chaves precisam ser únicas
d1['Nova chave'] = 'Valor nova chave'

print(d1[3])
'''
'''
d1 = {
    'k1': 'v1',
    'k2': 'v1',
    'k3': 'v3',
}

'''
'''
# print(d1.get('nomedachave'))  # pelo menos o código não para de funcionar
d1['str'] = 'agora existe'
'''
'''
# d1.update({'nova_chave':'novo_valor'})

if d1.get('str') is not None:
    print(d1.get('str'))

print(123)
'''
'''
d1['naoexiste'] = 'agora existe'

if 'naoexiste' in d1:
    print(d1['naoexiste'])

print('Oi')

'''
'''
print('str' in d1)
print('str' in d1.keys())
print('valor' in d1.values())
'''
'''
del d1['str']
print(d1)
'''
'''
for k, v in d1 and d1.items():
    print(k, v)

for k in d1.items():
    print(k[0])



'''
'''
clientes = {
    'cliente1':{
        'nome' : 'Lucas',
        'sobrenome':'Rosa',
    },
    'cliente2':{
        'nome': 'Marina',
        'sobrenome':'Faria',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')
'''
'''
d1 = {1: 'a', 2: 'b', 3: 'c'}
v = d1
print(d1)
print(v)  # nesse caso não está criando um novo dicionário, se alterar um, ambos são alterados
v = d1.copy()

v[1] = 'Lucas'
print(v)

'''
'''
v[1] = 'Luiz'

print(d1)
print(v)
'''
'''
import copy

d1 = {1: 'a', 2: 'b', 3: 'c', 4: ['Lucas', 'Rosa']}
v = copy.deepcopy(d1)

v[1] = 'Lucas'
v[4][0] = 'Ruca'

print(d1)
print(v)
'''
'''
d1 = {
    1: 2,
    2: 3,
    3: 4,
}
# d1.popitem()
# d1.pop(2)

d2 = {
    'a': 'b',
    'c': 'd',
}
d1.update(d2)
print(d1)
'''