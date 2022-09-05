'''
Funções (def) em python - *args **kwargs -
Aula 16 (parte 3)
'''
'''
def func (a1, a2, a3, a4, a5, nome=None, a6=None):
    print (a1, a2, a3, a4, a5, nome, a6)

var = func()

'''
'''
def func(*args, **kwargs):
    print(args)

    idade = kwargs.get('idade')

    if idade is not None:
        print(idade)
    else:
        print('Idade não existe')

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome = 'Lucas', sobrenome = 'Souza', idade='30')
'''

def func(*args, **kwargs):
    print(args)

    idade = kwargs['Idade']  #melhor usar get, se não tiver certeza de que existirá a chave
    print(idade)

lista = [1,2,3,4,5]
lista2 = [10,20,30,40,50]
func(*lista, *lista2, nome = 'Lucas', sobrenome = 'Souza', Idade = '27')