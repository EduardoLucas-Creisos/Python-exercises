#Exercício Python 52: Faça um programa que leia um número inteiro e diga se
# ele é ou não um número primo.
n = int(input('Digite um inteiro qualquer '))
p = 0
for c in range(1, n+1):
    d = n % c
    if d == 0 and (c != 1 or c != n):
       p = p+1


if p == 2:
    print('{} É primo'.format(n))
else:
    print('{} Não é primo'.format(n))

