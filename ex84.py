'''Exercício Python 084:
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''



maior = []
menor = []
l = []
peso = 0
nome = ''
cont = 0
s = ''
while True:
    nome = str(input('Digite seu nome: '))
    l.append(nome)
    peso = float(input('Digite seu peso: '))
    l.append(peso)
    if peso > 90 :
        maior.append(l[:])
    elif peso > 70 and peso < 89:
        pass
    else:
        menor.append(l[:])
    l.clear()
    cont +=1
    s = str(input('Quer continuar? [S/N] ')).lower().strip()
    if s == 's':
        pass
    elif s == 'n':
        break
    else:
        pass


print(f'Foram cadastradas {cont} pessoas')
print(f'As pessoas com o maior peso foram {maior}')
print(f'As pessoas com o menor peso foram {menor}')