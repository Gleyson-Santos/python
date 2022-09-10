import os


off = False
print('Hello, this is a two digit calculator.')
while not off:
    os.system('clear')
    n1 = ''
    while len(n1) != 2:
        n1 = input('Type a two digit number, please.\n')
    total = 0
    for digit in n1:
        total += int(digit)

    print(total)
    if input('Do you want to sum again? ') == 'no':
        off = True
        print('Bye bye!!!')
