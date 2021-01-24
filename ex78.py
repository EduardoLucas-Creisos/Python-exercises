'''Exercício Python 078:
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
 No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

x = []
ma = 0
me = 0
p1 = 0
p2 = 0
for p in range (0 , 5):
    x.append(int(input('Digite um número inteiro ')))
for c in range (0, 5) :
    if c == 0:
        ma = x[c]
        p1 = c
        me = x[c]
        p2 = c
    if c > 0 and ma < x[c]:
        ma = x[c]
        p1 = c
    if c > 0 and me > x[c]:
        me = x[c]
        p2 = c
print(f'O número {ma} é o maior dos números digitados e está na posição {p1}')
print(f'O número {me} é o menor dos números digitados e está na posição {p2}')