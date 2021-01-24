'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha
separados os valores pares e ímpares. No final,
mostre os valores pares e ímpares em ordem crescente.'''


l = [[], []]
x = 0
for c in range(0, 7):
    x = int(input('Digite um número inteiro: '))
    if x % 2 == 0:
        l[0].append(x)
    elif x % 2 != 0:
        l[1].append(x)

l[0].sort()
l[1].sort()
print(f'Os valores pares são {l[0]}')
print(f'Os valores ímpares são {l[1]}')
