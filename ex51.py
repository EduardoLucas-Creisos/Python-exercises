#Exercício Python 51: Desenvolva um programa que
# leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

n = int(input('Digite o primeiro termo '))
r = int(input('Digite a razão '))
s = n



for c in range(1, 10):
   print(' {} -->'.format(s), end='')
   s = s + r

print(' FIM!')