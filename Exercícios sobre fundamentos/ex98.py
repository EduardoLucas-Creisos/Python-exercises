'''Exercício Python 098:
Faça um programa que tenha uma função chamada contador(),
 que receba três parâmetros: início, fim e passo. Seu programa tem que realizar
 três contagens através da função criada:
            a) de 1 até 10, de 1 em 1
            b) de 10 até 0, de 2 em 2
            c) uma contagem personalizada'''
from time import sleep


def contador(ini, fim, cont):
    if cont == 0:
        cont = 1
    if ini > fim:
        sub = fim
        fim = ini
        ini = sub
    if cont < 0:
        sub = fim
        fim = ini
        ini = sub
    if cont < 0:
        print(f'Contado de {ini} até {fim-1} de {cont*(-1)} em {cont*(-1)}')
    else:
        print(f'Contado de {ini} até {fim-1} de {cont} em {cont}')
    for c in range(ini, fim, cont):
        print(f'{c}', end=' ')
        sleep(0.5)
    print()


print('a) de 1 até 10, de 1 em 1')
a = 1
b = 11
c = 1
contador(a, b, c)
print()
print('b) de 10 até 0, de 2 em 2')
a = 0
b = 10
c = -2
contador(a, b, c)
print()
print('c) uma contagem personalizada')
a = int(input('Digite o início: '))
b = int(input('Digite o fim: '))
c = int(input('Digite o contador: '))
contador(a, b, c)
