'''Exercício Python 101:
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascimento de uma pessoa, retornando um valor literal
indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.'''

import  datetime

def voto(ano):
    idade = datetime.date.today().year-ano
    situacao = ''

    if idade >= 18 and idade < 65:
        situacao = 'OBRIGATÓRIO'
    elif (idade < 18 and idade >= 16) or idade >= 65:
        situacao = 'OPCIONAL'
    else:
        situacao = 'NEGADO'
    return situacao, idade




#main

x = int(input('Digite seu ano de nascimento: '))
s = voto(x)
print(f'Visto que você tem {s[1]} anos de idadde')
print(f'A situação do seu voto é: {s[0]}')
