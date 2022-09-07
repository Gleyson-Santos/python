variavel = 'valor'


def func():
    print(variavel)


def func2():
    # variavel = 'outra valor'
    global variavel
    variavel = 'outra valor'
    print(variavel)


func()
func2()

