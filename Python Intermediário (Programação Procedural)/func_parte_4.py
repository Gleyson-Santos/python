variavel = 'valor'


def func(arg):
    print(variavel, 'func')
    arg = 'mudando valor'
    return arg


variavel = func('valor')


print(variavel)


def func2():
    # variavel = 'outra valor'
    global variavel
    variavel = 'outra valor'
    print(variavel, 'func2')


func2()

