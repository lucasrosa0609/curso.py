'''
- Criar variáveis para nome (str), idade (int), altura (float) e peso (float) de uma pessoa
- Criar variável com o ano atual (int)
- Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
- Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
- Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
'''

nome = 'Lucas de Souza Fernandes Rosa'
idade = 27
altura = 1.82
peso = 100.0
data_atual = 2022
imc = peso / 2**altura

print (f'{nome} tem {idade}, {altura} de altura e pesa {peso}kg')
print (f'o IMC de luiz é {imc:.2f}')
print (f'{nome} nasceu em', int(data_atual - idade))

# dava pra colocar o ano de nascimento como formatação de string pra facilitar caso o código fosse maior

num_1 = 2
num_2 = '2'
num_3 = num_1 * num_2