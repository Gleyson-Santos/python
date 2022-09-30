string = '0123456789012345678901234567890123456789012345678901234567890123456789'
new_str = ''
for number in string:
    new_str += number
    if number == '9':
        new_str += ','
# lista = [item for item in string if item == '9']
new_str2 = new_str.split(',')
retorno = '.'.join(new_str2)

print(retorno)
