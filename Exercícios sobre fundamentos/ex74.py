'''Exercício Python 074:
 Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla'''

import random

x = random.randint(0, 100)
s = random.randint(0, 100)
z = random.randint(0, 100)
w = random.randint(0, 100)
y = random.randint(0, 100)
n = (x, s, z, w, y)

print(sorted(n))
print('O maior valor foi {}'.format(max(n)))
print('O menor valor foi {}'.format(min(n)))

