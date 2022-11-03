"""
meta caracteres ^ $
[a-z]+
'(Luiz|Otavio)'
"""
import re
texto = '''
<p>Frase 1</p> <p>Eita</p> <p>Qualquer frase</p> <div>1</div> 
'''
cpf = '147.852.963-12'
print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
