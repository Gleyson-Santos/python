import math
PI = math.pi


def dobra_lista(lista):
    return [x * 2 for x in lista]


def multiplica(lista):
    r = 1
    for item in lista:
        r *= item

    return r


lista1 = list(range(5))

if __name__ == '__main__':
    print(dobra_lista(lista1))
    print(PI)
