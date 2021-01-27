'''Exercício Python 091:
 Crie um programa onde 4 jogadores joguem um dado e tenham
  resultados aleatórios. Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.'''
import operator
import time
import random
menor = 0
jogo = {'jogador1': 0, 'jogador2': 0, 'jogador3': 0, 'jogador4': 0}
rank = []
for k in jogo.keys():
    x = random.randint(1, 6)
    jogo[k] = x


menor = jogo['jogador1']

for k, v in jogo.items():
    print(f'{k} = {v}')
rank = sorted(jogo.items(), key=operator.itemgetter(1), reverse = True)
for i, v in enumerate(rank):
    print(f'{i+1} posição: {v[0]} com {v[1]} ')
    time.sleep(1)









