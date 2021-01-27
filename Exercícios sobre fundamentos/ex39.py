#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e
# informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já
# passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

ano = int(input('Digite o ano de nascimento '))

idade = 2021 - ano

if(idade == 18):
    print('Esse é o momento certo de se alistar')
elif(idade > 18):
    t = idade - 18
    print('Você  passou do tempo de se alistar a {} anos '.format(t))
    print('Você devia ter se alistado no ano de {}'.format(2021 - t))
else:
    t = 18 - idade
    print('Você ainda é jovem faltam {} anos para você se alistar '.format(t))
    print('Você deve se alistar no ano de {}'.format(2021 + t))