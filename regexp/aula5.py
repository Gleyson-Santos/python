"""
meta caracteres ^ $
[a-z]+
'(Luiz|Otavio)'
"""
import re
from pprint import pprint
texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''
# cpf = '147.852.963-12'
# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

tags = re.findall(r'(<([dpiv]{1,3})>.+?</\2>)', texto, flags=re.I)
# pprint(tags)

for tag in tags:
    um, dois = tag
    pprint(um)

