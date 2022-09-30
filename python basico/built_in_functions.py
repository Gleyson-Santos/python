"""
Built in functions
Python não faz conversão automática
isnumeric isdigit isdecimal -> numeros e positivos (não chega numeros reais/flutuantes)
"""
num1 = input('Digite um numero: ')
num2 = input('Digite outro número ')
num3 = input('Digite outro número ')

num1_convertido = int(num1) if num1.isnumeric() else 'Não pode ser convertido'
num2_convertido = int(num2) if num2.isdigit() else 'Não pode ser convertido'
num3_convertido = int(num3) if num3.isdecimal() else 'Não pode ser convertido'

print(num1_convertido)
print(num2_convertido)
