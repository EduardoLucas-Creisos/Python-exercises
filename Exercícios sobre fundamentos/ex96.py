'''Exercício Python 096:
Faça um programa que tenha uma função chamada área(),
que receba as dimensões de um terreno retangular (largura e comprimento) e
mostre a área do terreno.'''


def area(base, altura):
    a =  base * altura
    print(f'A área do terreno corresponde à {base} x {altura} = {a}')


l = int(input('Digite a largura: '))
c = int(input('Digite  o comprimento: '))

area(l, c)
