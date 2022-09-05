'''
Iniciar com letra, pode conter números, separar _, letras minúsculas
'''

nome = 'Lucas de Souza Fernandes Rosa'
data_nascimento = 1995
data_atual = 2022
idade = (data_atual - data_nascimento)
altura = 1.80
maior_idade = idade > 18
peso = 100
imc = (peso // (altura *2))

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior de idade?:', maior_idade)
print (nome, 'tem', idade, 'anos de idade e seu imc é', imc)
