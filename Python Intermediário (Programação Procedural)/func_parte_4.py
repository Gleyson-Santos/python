variavel = 'valor'


def func():
    print(variavel, 'func')


def func2():
    # variavel = 'outra valor'
    global variavel
    variavel = 'outra valor'
    print(variavel, 'func2')


func()
func2()

