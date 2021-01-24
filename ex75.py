'''Exercício Python 075:
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
 No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.'''
x = 0
z = 0
po = 0
pa = 0
c = (int(input('Digite um número \n')),
     int(input('Digite um número \n')),
     int(input('Digite um número \n')),
     int(input('Digite um número \n')))
for x in range(0, 4):
    if 9 == c[x]:
        z += 1
    else:
        pass
    if c[x]%2 == 0:
        pa += 1
    else:
        pass
for x in range(0, 4):
    if 3 == c[x]:
        po = x
        po = po + 1
        break
    else:
        pass
print('O número de vezes que o número 9 foi digitado foi {} '.format(z))
if po > 0:
    print('O número 3 foi digitado na {}° posição '.format(po))
print('O total de números pares foi {} '.format(pa))







