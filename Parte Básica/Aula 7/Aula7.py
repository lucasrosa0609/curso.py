nome = 'Lucas de Souza Fernandes Rosa'
data_nascimento = 1995
data_atual = 2022
idade = (data_atual - data_nascimento)
altura = 1.80
maior_idade = idade > 18
peso = 100
imc = (peso // (altura **2))

print (nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print (f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}') #f é como manipulamos a string, após a exibição de números o .2f é pela exibição da qtde de casas decimais
print ('{0} tem {1} anos e seu imc é {2}'.format (nome, idade, imc))
print ('{2} {0} tem {2} {1} anos e seu imc é {2}'.format (nome, idade, imc)) #dá pra mudar a formatação pelas chaves
print ('{n} {im} tem {i} {im} anos e seu imc é {n}'.format (n=nome, i=idade, im=imc))
