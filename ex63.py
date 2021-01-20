'''Exercício Python 63: Escreva um programa que leia um número N
inteiro qualquer e mostre na
tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:'''
print('-'*30)
n = int(input('Digite quantos termos você quer mostrar  '))
print('-'*30)
n1 = 0
n2 = 1
s = 0
print('0 --->',end='')
while n > 0:
    s = n1 + n2
    n2 = n1
    n1 = s
    print(' {} ---> '.format(s), end='')
    n = n - 1
    if n == 0:
        print(' Acabou')
