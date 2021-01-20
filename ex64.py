'''Exercício Python 64:
 Crie um programa que leia vários números inteiros pelo teclado.
 O programa só vai parar quando o usuário digitar o valor 999,
 que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles
  (desconsiderando o flag).

'''

n = int(input('Digite um inteiro qualquer '))
p = 0
s = 0
while n != 999:
    p += 1
    s += n
    n = int(input('Digite um inteiro qualquer '))

print('Você digitou {} números que somam igual a {} '.format(p, s))







