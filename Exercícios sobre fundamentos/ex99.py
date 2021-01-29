'''Exercício Python 099: Faça um programa que tenha uma função chamada maior(),
 que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior'''


def maior(* num):
    maior = x = 0

    for v in num:
        if x == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        x += 1

    print(f'De todos o {x} valores informados o maior é {maior}')





#main

maior(1, 2, 4, 65, 3 ,24 ,3 , 6, 8 ,7)






