'''
Operador ternário em python
'''
'''
logged_user = True
# logged_user = False
if logged_user:
    msg = 'Olá, seu safado sem vergonha'
else:
    msg = 'Faz o login direito ai o arrombadinho'

print(msg)'''
'''
logged_user = True
msg = 'Usuário logado' if logged_user else 'Usuário precisa fazer login'

print(msg)
'''
'''
idade = 18

if idade >= 18:
    print('Pode acessar')
else:
    print('Tem q ser di maior')
    
msg = 'Pode acessar' if idade >= 18 else 'Não pode acessar'

'''

idade = input('Qual sua idade? ')
if not idade.isnumeric():
    print('Precisa escrever apenas números')
else:
    idade = int(idade)
    maior = (idade >= 18)
    msg = 'Pode acessar' if maior else 'Não pode acessar'
    print(msg)