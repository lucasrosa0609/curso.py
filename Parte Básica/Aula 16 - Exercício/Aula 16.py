'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um numero
inteiro, informa que não é um número inteiro
'''

num1 = input('Digite um número: ')

if num1.isdigit():
    num1 = int(num1)

    if num1 % 2 == 0:
        print(f'{num1} é um número par')
    else:
        print(f'{num1} é um número ímpar')
else:
    print ('Favor digitar um número inteiro.')

'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada.
Ex: Bom dia 0-11, boa tarde 12-17 e boa noite 18-23
'''

hora_usuario = input('Qual é o horário agora? ')


if hora_usuario.isdigit():
    hora_usuario = int(hora_usuario)
    if hora_usuario >= 0 and hora_usuario <= 11:
        print(f'{hora_usuario} É pela manhã! Bom dia!')
    elif hora_usuario >= 12 and hora_usuario <= 17:
        print(f'{hora_usuario} é horário da tarde. Boa tarde')
    elif hora_usuario >= 18 and hora_usuario <= 23:
        print(f'{hora_usuario}!! Boa noite')

else:
    print('Por favor, digite o horário com números')

'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos
escreva 'Seuu nome é curto'; se tiver entre 5 e 6 letras, escreva 'Seu nome é normal';
Se for maior que 6, escreva 'Seu nome é muito grande'
'''

nome_usuário = input('Qual seu primeiro nome?: ')

if len(nome_usuário) <= 4:
    print('Seu nome é muito curto')
elif len(nome_usuário) > 4 and len(nome_usuário) <= 6:
    print ('Seu nome é normal')
elif len(nome_usuário) > 6:
    print('Seu nome é muito grande')
