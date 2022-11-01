import form1


def aumento(valor, porcentagem, arg=False):
    if arg:
        return form1.preco.real(valor)
    return valor + (valor * porcentagem / 100)


def reduz(valor, porcentagem, arg=False):
    if arg:
        return form1.preco.real(valor)
    return valor - (valor * porcentagem / 100)
