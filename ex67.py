'''Exercício Python 67:
 Faça um programa que mostre a tabuada de vários números,
  um de cada vez, para cada valor digitado pelo usuário.
  O programa será interrompido quando o número solicitado for negativo.'''


n = 0
while True:
    n = int(input('Digite um número inteiro qualquer '))
    if n < 0:
        print('Programa finalizado')
        break
    for c in range (1, 11):
        print(f' {n} x {c} = {n*c} ')


