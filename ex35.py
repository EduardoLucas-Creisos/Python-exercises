#Exercício Python 035: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
import math
dis = float(input('Digite a distância '))
dis = math.trunc(dis)
if dis > 200:
    valor = dis * 0.45
    print('O valor da viagem é {}'.format(valor))
else:
    valor = dis * 0.5
    print('O valor da viagem é {}'.format(valor))