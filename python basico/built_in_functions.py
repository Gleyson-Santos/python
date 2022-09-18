"""
Built in functions
"""
num1 = input('Digite um numero: ')
num2 = input('Digite outro número ')
num1_convertido = int(num1) if num1.isdigit() else 'Não pode ser convertido'
num2_convertido = int(num2) if num1.isdigit() else 'Não pode ser convertido'
print(num1_convertido)
print(num2_convertido)
