#Exercício Python 53:
# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços. Exemplos de palíndromos:

frase = input('Digite uma frase ').strip().upper()
p = frase.split()
j = ''.join(p)
i = ''
for c in range(len(j) - 1, -1, -1):
    i += j[c]
print('O inver so de {} é {} '.format(j, i))
if i == j:
    print('{} é um palíndromo '.format(frase))
else:
    print('{} não é um palíndromo '.format(frase))