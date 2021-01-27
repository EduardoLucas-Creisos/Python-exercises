#Exercício Python 031: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input('Digite um ano '))
if ano % 4 == 0:
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))
