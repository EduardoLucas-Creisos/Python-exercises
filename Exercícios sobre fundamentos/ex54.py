#Exercício Python 54:
# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
import  datetime
hoje = datetime.date.today().year
maior = 0
menor = 0
for c in range (0, 7):
    ano = int(input('Digite o seu ano de nascimento '))
    if hoje-ano >= 18:
        maior += 1
    else:
        menor +=1

print('O número de pessoas maiores de idade é {} e de menores é {}'.format(maior, menor))
