#Exercício Python 56:
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

m = 0
mu = 0

for c in range(0, 4):
    print('----{}º PESSOA----'.format(c+1))
    nome = input('Digite seu nome ')
    sexo = input('Digite seu sexo ').lower()
    idade = int(input('Digite sua idade '))
    m += idade
    if c == 0 and sexo == 'masculino':
        maisi = idade
        mais = nome
    elif c == 0 and sexo == 'feminino':
        maisi = 0
        mais = ''
    if c != 0 and sexo =='masculino':
        if maisi == 0 and mais == '':
            mais = nome
            maisi = idade
        elif maisi < idade:
            mais = nome
            maisi = idade
    if sexo == 'feminino' and idade < 20:
        mu += 1


m = m/4
print('A média de idade do grupo é {}'.format(m))
print('O homem mais velho é {} ele tem {}'.format(mais, maisi))
print('Tem {} mulheres com menos de 20 anos'.format(mu))







