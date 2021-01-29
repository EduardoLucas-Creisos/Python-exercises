'''Exercício Python 103:
 Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
 o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz
de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.'''


def ficha(nome = '', gols = 0):
    ficha = ''
    if nome == '':
        ficha += '<<jogador desconhecido>> marcou '
        ficha += (f' {gols} gols no campeonato!')
    else:
        ficha += (f'{nome} marcou')
        ficha += (f' {gols} gols no campeonato!')
    return print(ficha)


#main

nome = str(input('Digite o nome do jogador: '))
gols = str(input('Digite quantos gols ele marcou no campeonato: '))
if gols == '':
    gols = '0'
if gols.isnumeric():
    gols = int(gols)
else:
    gols = int(0)

ficha(nome,gols)