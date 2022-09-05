# class CarrinhoDeCompras:
#     def __init__(self):
#         self.produtos = []
#
#     def inserir_produto(self,produto):
#         self.produtos.append(produto)
#
#     def lista_produto(self):
#         for produto in self.produtos:
#             print(f' {produto.nome}, R${produto.valor}')
#
#     def soma_total(self):
#         total = 0
#         for produto in self.produtos:
#             total += produto.valor
#         return total
#
# class Produto:
#     def __init__(self, nome, valor):
#         self.nome = nome
#         self.valor = valor

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def insere_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_endereco(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} FOI APAGADE')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado
