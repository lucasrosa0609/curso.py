'''
Tipos de dados
str - string (textos) 'assim' ou ''assim''
int - inteiro - 123456 (número positivo, negativo ou 0, que não tenha ponto)
float - nº real ou ponto flutuante - negativo, positivo ou 0 que tenha ponto - 10.50; 1.5; -10.10; -50.93
bool - booleano/lógico -  só tem 2 valores - true/false (comparações) 10 == 10
'''

'''
print ('luiz', type('Luiz'))
print ('10', type(10))
print ('10.5', type(10.5))  # se o número for colocado entre aspas, ele se comporta como uma str
print ('10' == '10.5', type(10 == 10))
print (bool())
'''

# print('luiz', type('luiz'), bool('luiz'))

# print('10', type('10'), type(int('10'))) #conversão do tipo pra int, o que nem sempre é possível

# print ('luiz', int('luiz')) #esse não funciona, já que estou tentando converter texto em número

print ('luiz', float (10)) #pode fazer com numeros inteiros ou próprios de floats
print ('luiz', float (10+10))
print ('10+10') #vai resultar em 10+10, se tirar as aspas ele fará as contas


