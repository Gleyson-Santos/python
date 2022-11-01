import re

# findall, search, sub, compile
string = 'Este é um teste de expressões teste regulares.'
print(re.findall(r'teste', string))
print(re.search(r'teste', string))
print(re.sub(r'teste', 'ABCD', string, count=1))

regexp = re.compile(r'teste')
print(regexp.findall(string))
print(regexp.search(string))
print(regexp.sub('def', string))
