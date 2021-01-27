#Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input('Digite a velocidade '))
if vel >= 80:
    multa = 7+((vel-80)*7)
    print('Você foi multado em {} reais'.format(multa))
else:
    print('Tudo tranquilo')

