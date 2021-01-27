#Exercício Python 55:
# Faça um programa que leia o peso de cinco pessoas. No final,
# mostre qual foi o maior e o menor peso lidos.
ma = 0
me = 0
atual = 0
for c in range(0, 5):
    peso = float(input('Digite seu peso '))
    atual = peso
    if c == 0:
        ma = atual
        me = atual
    else:
        if atual >= ma:
            ma = atual
        if atual <= me:
            me = atual






print('O maior peso é {} e o menor é {}'.format(ma, me))

