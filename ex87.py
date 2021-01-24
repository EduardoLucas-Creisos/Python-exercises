'''Exercício Python 087:
 Aprimore o desafio anterior, mostrando no final:
  A) A soma de todos os valores pares digitados.
  B) A soma dos valores da terceira coluna.
  C) O maior valor da segunda linha.

'''

matriz = [[], [], []]
x = 0
c = 1
l = 1
soma = 0
soma1 = 0
maior = 0
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
        if l == 1 and c == 0:
            maior = matriz[l][c]

        if l == 1 and matriz[l][c] > maior:
            maior = matriz[l][c]

        if c == 2 :
            soma1 += matriz[l][c]

        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]

    print()
print(f'A soma dos valores pares é {soma}')
print(f'A soma dos valores da 3º coluna é {soma1}')
print(f'O maior valor da segunda linha é {maior}')
