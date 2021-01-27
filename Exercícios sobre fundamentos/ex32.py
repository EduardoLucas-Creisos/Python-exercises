#Exercício Python 032: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite um número interio '))
n2 = int(input('Digite um número interio '))
n3 = int(input('Digite um número interio '))

ma = n1
me = n1
if n2 > n1 & n2 > n3:
    ma = n2
else:
    if n3 > n1:
        ma = n3

if n2 < n1 & n2 < n3:
    me = n2
else:
    if n3 < n1:
        me = n3




print('O maior valor é {} e o menor é {}'.format(ma, me))