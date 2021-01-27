'''Exercício Python 088:
Faça um programa que ajude um jogador da MEGA SENA a criar
 palpites.O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''

import random
import time
x = 0
njogos = 0
jogos = []
njogos = int(input('Quantos palpites você quer? '))+1
lista = []
while True:
   for c in range(0, 6):
    x = random.randint(1 ,60)
    if x not in jogos:
           jogos.append(x)
    else:
           while x not in jogos:
               x = random.randint(1, 60)
           jogos.append(x)

   njogos -= 1
   if njogos == 0:
     break
   lista.append(jogos[:])
   jogos.clear()
for y in range (len(lista)):
    print(lista[y])
    time.sleep(1)

