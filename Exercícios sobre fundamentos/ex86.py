'''Exercício Python 086:
 Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores
lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.'''

matriz = [[], [], []]
x = 0
c = 1
l = 1
for y in range(0, 9):
    x = int(input(f'Digite um número que será colocada na coluna {l} da linha {c} '))
    l += 1
    if y < 3:
        matriz[0].append(x)
    elif y < 6 and y > 2:
        matriz[1].append(x)
    elif y < 9 and y > 5:
        matriz[2].append(x)
    if l  == 4:
        c += 1
        l = 1


for l in range (0, 3):

    for c in range (0, 3):
        print(f'({matriz[l][c]})', end= '  ')

    print()


#print(f'({matriz[1][0]})   ({matriz[0][1]})   ({matriz[0][2]})  ')
#print(f'({matriz[1][0]})   ({matriz[1][1]})   ({matriz[1][2]})  ')
#print(f'({matriz[2][0]})   ({matriz[2][1]})   ({matriz[2][2]})  ')
