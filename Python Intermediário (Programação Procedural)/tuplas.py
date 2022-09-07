"""
Tuplas em Python
"""

t1 = (1, 2, 3, 'a', 'Gleyson Santos')
t2 = 6, 7, 8, 9, 10
t1 += t2
# for i in t1:
#     print(i)

# print(type(t2))
n1, n2, *_ = t1 * 20

# print(n1)
# print(n2)
print(_)
