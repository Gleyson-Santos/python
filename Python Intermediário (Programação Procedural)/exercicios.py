"""
1 - Crie uma função que exibe uma saudação com os párâmetros saudação e nome.
"""


def func1(msg, nome):
    msg = f"Exercicio 1: {msg} {nome}"
    print(msg)


func1('Hello', 'Gleyson')

"""
2 - Crie uma função que receba 3 números como parâmetros e exiba a soma entre eles.
"""


def func2(n1, n2, n3):
    soma = n1 + n2 + n3
    print(f"Exercicio 2: {soma}")

func2(1, 2, 3)
"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do 
primeiro número somado do aumento do percentual do mesmo.
"""


def func3(n1, percentual):
    return n1 + (n1 * percentual / 100)


x = func3(50, 10)
y = func3(100, 10)
z = func3(10, 10)
k = func3(15, 100)
print(f"Exercicio 3: {x}")
print(f"Exercicio 3: {y}")
print(f"Exercicio 3: {z}")
print(f"Exercicio 3: {k}")

"""
4 - Fizz Buzz
"""
print("Exercicio 4")


def func4(n1):
    for number in range(n1 + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


func4(100)
