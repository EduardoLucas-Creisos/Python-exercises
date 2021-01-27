#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça
# para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
import math
num = int(input('Digite um número qualquer '))

print('Digite  1-para converter esse número para binário ')
print('Digite  2-para converter esse número para octal ')
print('Digite  3-para converter esse número para hexadecimal ')
x = int(input())
if (x == 1):
    print('O número {} em binário é {}'.format(num, bin(num)[2:]))

elif (x == 2):
    print('O número {} em octal é {}'.format(num, oct(num)[2:]))

elif (x == 3):
    print('O número {} em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida')
