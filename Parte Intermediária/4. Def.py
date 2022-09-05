'''
Escopo de variável
'''
'''
v = 'valor'  # escopo global

def func():
    print(v)

def func2(arg=None):
    arg = arg.replace('v', 'c')
    return arg

func()
o_v = func2(arg=v)  # executar a função precisa dessa node

print(o_v)
'''
'''
v = 'valor'

def func():
    print(v)
    v = 1234  # vai dar erro, pra variável local, precisa trocar a variável ANTES
    print(v)

func()
'''

v = 'valor'

def func():
    o_v = 'Lusca'
    return o_v

def func2(arg):
    print(arg)

var = func()
func2(var)
