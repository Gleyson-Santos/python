d1 = {
    'str' : 'valor',
    123 : 'Outro Valor',
    (1, 2, 3, 4) : 'Tupla',
}

if d1.get('nomedachave') is not None:
    print(d1.get('nomedachave'))

print(123)
