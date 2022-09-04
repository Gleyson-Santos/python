frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

# while contador < 10:
#     print(contador)
#     contador += 1
input_do_usuario = input("Digite uma letra: ")
# iteração, iterando, iterar -> percorrer cada um dos elementos iteraveis
while contador < tamanho_frase:
    # print(frase[contador], ':', contador)
    letra = frase[contador]
    if letra == input_do_usuario:
        nova_string += input_do_usuario.upper()
    else:
        nova_string += letra
    print(nova_string)
    contador += 1

print(nova_string)
