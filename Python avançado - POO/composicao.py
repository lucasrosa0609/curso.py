from classes import Endereco, Cliente


cliente1 = Cliente('Luiz', 32)
cliente1.insere_endereco('Belo Horizonte', 'MG')
print(cliente1.nome, cliente1.idade)
cliente1.lista_endereco()

print()

cliente2 = Cliente('Marina', 55)
cliente2.insere_endereco('Sao Jose dos Campos', 'SP')
cliente2.insere_endereco('Caraguatatuba', 'SP')
print(cliente2.nome, cliente2.idade)
cliente2.lista_endereco()

print()

cliente3 = Cliente('Lucas', 27)
cliente3.insere_endereco('Sao Jose dos Campos', 'SP')
print(cliente3.nome, cliente3.idade)
cliente3.lista_endereco()
