'''
Exercício Python 65:
 Crie um programa que leia vários números inteiros pelo teclado.
 No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
  O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

x = int(0)
n = int (0)
m = int(0)
d = int(0)
while x > -1:
    n= int(input('Digite um número '))
    if x == 0:
        ma = n
        me = n
    if x > 0 :
        if n > ma:
            ma = n
        if n < me:
            me = n
    m += n
    x +=1
    d += 1
    conf = input('Deseja continuar? [S/N] ').upper()
    if conf == 'N':
        x = -1
print('Você digitou {} números cujo o maior foi {} e o menor foi {} a média deles foi {:.2f}'
      .format(d, ma, me, m/d))
