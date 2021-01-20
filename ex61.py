'''Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro
 termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
 usando a estrutura while.

'''

n = int(input('Digite o primeiro termo '))
r = int(input('Digite a razão '))
s = n
x = 0

while x < 10:
    print(' {} -->'.format(s), end='')
    s = s + r
    x += 1
print('FIM!')