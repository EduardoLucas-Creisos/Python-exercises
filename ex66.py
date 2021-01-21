'''Exercício Python 66:
 Crie um programa que leia números inteiros pelo teclado.
  O programa só vai parar quando o usuário digitar o valor 999,
   que é a condição de parada. No final, mostre quantos números foram digitados e qual
    foi a soma entre elas (desconsiderando o flag).

'''
n = 0
s = 0
cont = 0
while True:
    n = int(input('Digite um inteiro qualquer '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Você digitou {cont} números que somados são iguais a {s}')
