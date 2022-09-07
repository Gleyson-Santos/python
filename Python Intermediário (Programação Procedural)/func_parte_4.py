variavel = 'valor'


def func():
    global variavel
    print(variavel)
    variavel = 1234
    print(variavel)


func()
