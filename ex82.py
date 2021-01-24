'''Exercício Python 082:
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
 respectivamente. Ao final, mostre o conteúdo das três listas geradas.

'''


n = []
par = []
impar = []

for c in range (0 , 21):
    n.append(int(input('Digite um numero ')))
    if n[c] % 2 == 0:
        par.append(n[c])
    elif n[c] % 2 != 0:
        impar.append(n[c])
print(f'A lista de números digitados foi {n}')
print(f'A lista contendo somente os números pares foi {par}')
print(f'A lista contedo somente os números ímpares foi {impar}')