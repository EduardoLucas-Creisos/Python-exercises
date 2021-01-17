#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
num = int(input('Digite um número '))
n = num % 2
if n == 0:
    print("{} é par".format(num))
else:
    print("{} é ímpar".format(num))