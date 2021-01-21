'''Exercício Python 68:
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

'''

import  random
jogador = ''
computador = ''
c = 0
n = 0
s = 0
cont = 0
while True:
    jogador = input('Escolha entre par ou ímpar ').upper()
    while jogador != ('PAR') and jogador != ('ÍMPAR'):
        print('Opção inválida tente novamente')
        jogador = input('Escolha enter par ou ímpar ').upper()
    if jogador == 'PAR':
        computador ='ÍMPAR'
    elif jogador == 'ÍMPAR':
        computador = 'PAR'
    c = random.randint(0, 10)
    n = int(input('O computador escolheu um número tente vecer ele no jogo do ímpar ou par escolhendo um númreo inteiro '))
    print(f'O computador escolheu {c} e você escolheu {n}')
    s = c+n
    if s % 2 == 0:
        if  jogador == 'PAR':
            cont += 1
            print('Você venceu')
        else:
            print('O computador venceu')
            break
    else:
        if jogador == 'ÍMPAR':
            cont += 1
            print('Você venceu')
        else:
            print('O computador venceu')
            break
print(f'O número de vezes que você venceu foi {cont}')

