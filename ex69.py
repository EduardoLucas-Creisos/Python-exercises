'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
 A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
 No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.

'''

maior = 0
homem = 0
m20 = 0
idade = 0
sexo = ''
s = ''
x = ''
y = ''
while True:
    idade = int(input('Qual a sua idade? '))
    if idade >= 18:
        maior += 1
    sexo = str(input('Qual seu sexo? ')).upper().strip()
    s = sexo.strip()[0]
    while 'M' not in s and 'F' not in s:
        print('Opção inválida tente novamente ')
        sexo = str(input('Qual seu sexo? ')).upper().strip()
        s = sexo.strip()[0]
    if 'M' in s:
        homem += 1
    if 'F' in s and idade < 20:
        m20 += 1
    x = str(input('Deseja continuar cadastrando? \n'
                  'Digite "Sim" para continuar ou digite qualquer coisa para parar ')).upper().strip()
    y = x.strip()[0]
    if 'S' in y:
        pass
    else:
        break
print(f'O número de pessoas com mais de 18 anos cadastradas é {maior}')
print(f'O número de homens cadastrados é {homem}')
print(f'O número de mulheres com menos de 20 anos é {m20}')




