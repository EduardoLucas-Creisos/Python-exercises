'''Exercício Python 092:
 Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
  cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
   o dicionário receberá também o ano de contratação
e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''

import datetime
pessoa = dict()

pessoa['nome'] = input('Digite o nome: ')
anona = int(input('Digite seu ano de nascimento: '))
pessoa['idade'] = datetime.datetime.now().year - anona
pessoa['carteira '] = int(input('Digite o número da sua carteira de trabalho: '))
if pessoa['carteira '] != 0:
    pessoa['anocon'] = int(input('Digite o ano de sua contratação: '))
    pessoa['salario'] = float(input('Digite seu salário: '))
    pessoa['apo'] = pessoa['idade']+((pessoa['anocon']+35) - datetime.datetime.now().year)
for k, v in pessoa.items():
    print(f'{k} tem valor {v}')