#Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
import random
p = 'pedra'
pa = 'papel'
t= 'tesoura'
lista = (p, pa, t)
mao = random.choice(lista)
player = input('Digite pedra, papel ou tesoura ')
print('O computador jogou {}'.format(mao))
if(mao == p and player == 'papel'):
    print('O jogador ganhou')
elif(mao == p and player == 'pedra'):
    print('Empate')
elif(mao == p and player == 'tesoura'):
    print('O jogador perdeu')
elif(mao == pa and player == 'pedra'):
    print('O jogador perdeu')
elif(mao == pa and player == 'papel'):
    print('Empate')
elif(mao == pa and player == 'tesoura'):
    print('O jogador ganhou')
elif(mao == t and player == 'pedra'):
    print('O jogador ganhou')
elif(mao == t and player == 'papel'):
    print('O jogador perdeu')
elif(mao == t and player == 'tesoura'):
    print('Empate')
else:
    print('Configuração inválida')
