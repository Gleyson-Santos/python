cpf = "359.221.638-41"

true = True
while true:
    if '.' in cpf and '-' in cpf:
        cpf = cpf.replace('.', '')
        cpf = cpf.replace('-', '')
        true = False

print(cpf)

# total = 0
# for x, y in enumerate(new_cpf[:-2]):
#     print(x, ':', int(y))
