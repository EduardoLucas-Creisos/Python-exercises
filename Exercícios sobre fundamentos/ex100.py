'''Exercício Python 100:
 Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
  A primeira função vai sortear 5 números e vai colocá-los dentro
   da lista e a segunda função vai mostrar a
 soma entre todos os valores pares sorteados pela função anterior.'''

from random import randint
def somapar(num):
    x = soma = 0
    for c in num:
        if c % 2 == 0:
            soma += c
        else:
            pass
    print(f'A soma dos números pares foi {soma}')



def sorteia(x):

    for c in range(0, 5):
        x.append(randint(1, 20))

    print(f'Os 5 valores sorteados foram {x}')


#main
y = list()
sorteia(y)
somapar(y)