'''Exercício Python 071:
Crie um programa que simule o funcionamento de um caixa eletrônico. No início,
 pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas
 de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.'''

valor = int (input('Digite um valor a ser sacado '))
vi = valor
n50 = 0
n20 = 0
n10 = 0
n1 = 0
m = 0
nt = 0

while True:
    if valor >= 50:
        n50 = valor // 50
        nt += n50
        m = n50 * 50
        valor = valor - m
    if valor >= 20 and valor < 50:
        n20 = valor // 20
        nt += n20
        m = n20 * 20
        valor = valor - m
    if valor >= 10 and valor < 20:
        n10 = valor // 10
        nt += n10
        m = n10 * 10
        valor = valor - m
    if valor >= 1 and valor < 10:
        n1 = valor // 1
        nt += n1
        m = n1 * 1
        valor = valor - m
    if valor == 0:
        break
print(f'O valor solicitado de {vi}R$ será sacado em')
print(f'Cédulas  {n50} de 50R$')
print(f'Cédulas  {n20} de 20R$')
print(f'Cédulas  {n10} de 10R$')
print(f'Cédulas {n1} de 1R$')
print(f'O total de cédulas foi {nt}')













