'''Exercício Python 58:
Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.'''

import random

n = 1
r = random.randint(1, 10)
escolha = int(input('Tente adivinhar qual o número que o computador escolheu entre 1 e 10 '))

while escolha != r:
    print('Você errou')
    escolha = int(input('Tente adivinhar qual o número que o computador escolheu entre 1 e 10 '))
    n += 1
print('Você acertou o número escolhido era {}, você levou apenas {} tentativas para acertar '.format(r, n))
