'''Exercício Python 70:
 Crie um programa que leia o nome e o preço de vários produtos.
 O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.'''



nome = ''
barato = ''
preço = 0
menor = 0
total = 0
m1000 = 0
c = 0
x = ''
y = ''
while True:
    nome = str(input('Digite o nome do produto - '))
    preço = float(input('Digite o preço do produto em R$ '))
    total += preço
    if c == 0:
        menor = preço
    if preço < menor and c > 0:
        menor = preço
    if preço >= 1000:
        m1000 += 1
    if preço == menor:
        barato = nome

    x = str(input('Deseja continuar cadastrando? \n'
                  'Digite "Sim" para continuar ou digite qualquer coisa para parar ')).upper().strip()
    y = x.strip()[0]
    if 'S' in y:
        pass
    else:
        break


    c += 1
print(f'O valor total de todos os produtos é {total:.2f}R$')
print(f'O número de produtos acima de 1000 reais é {m1000}')
print(f'O produto mais barato é {barato} ele custa {menor:.2f}R$')