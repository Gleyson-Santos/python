import copy
d1 = {
    1: 'a',
    2: 'b',
    3: 'c',
    'd': 'Joãozinho',
}

v = copy.deepcopy(d1)
v['d'] = 'Bruninha'

print(v, d1)
print(v != d1)
