'''
Contagem de caracteres de uma string

não funciona com sistemas numéricos
'''

'''
usuario= input('Digite seu usuário: ')
qtde_caractere = len(usuario)

print(usuario, qtde_caractere, type(qtde_caractere))
if qtde_caractere <= 6:
    print('Favor reveja seu usuário pra pelo menos 6 caracteres')
else:
    print('Parabéns, você acertou a qtde de caracteres')
'''

string1 = input('Digite alguma coisa: ')
string2 = input('Digite outra coisa: ')

print(f'A quantidade total de caracteres digitados foi {len(string1)+len(string2)}')

print(len(string2))
print(string2.__len__())  # não funciona com int, float e bool

