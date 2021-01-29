'''Exercício Python 104:
 Crie um programa que tenha a função leiaInt(), que vai funcionar de
 forma semelhante ‘a função input() do Python,
 só que fazendo a validação para aceitar apenas um valor numérico.
 Ex: n = leiaInt(‘Digite um n: ‘)'''


def LeiaInt(msg):
    print(msg, end='')
    validador = False
    while True:
        p = str(input())
        if p.isnumeric():
            v = int(p)
            validador = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido. \033[m')
            pass
        if validador == True:
            break
    return v



#main

n = LeiaInt('Digite um número: ')
print(f'Você digitou {n}')



