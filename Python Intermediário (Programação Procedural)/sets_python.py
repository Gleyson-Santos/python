"""
add (adiciona), update (atualiza), clear, dicard
union | une
intersection & (todos os elementos presentes nos dois sets)
difference - (elementso apenas no set da esquerda)
symetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
"""
# set
s1 = set()  # apenas elementos imútaveis
print(s1)
s1.add(1)
s1.add(2)
print(s1)
s1.update('3')
s1.update('python')
s = ''
for x in s1:
    s += str(x)
s += 'ptttrruuu'
s1.update(s)

print(s1)

