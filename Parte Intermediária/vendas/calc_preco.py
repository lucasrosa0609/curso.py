
from cursopython.Parte Intermediária.vendas.formata.calc_preco import

def aumento(valor, porcentagem, formata=False):
    r = valor + (valor * (porcentagem / 100))
    return r

    if formata:
        return preco.real(r)
    else:
        return r

def reducao(valor, porcentagem, formata=False):
    r = valor - (valor * (porcentagem / 100))
    return r

    if formata:
        return preco.real(r)
    else:
        return r
