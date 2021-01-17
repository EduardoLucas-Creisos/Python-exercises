#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
num = random.randint(0, 5)
n = int(input('Tente adivinhar qual número de 0 a 5 o computador escolheu '))
if num==n:
    print('Parabéns você acertou')
else:
    print('que pena você errou')
print('O número escolhido foi {}'.format(num))