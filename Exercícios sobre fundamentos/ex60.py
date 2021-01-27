'''Exercício Python 060:
 Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:'''

n = int(input('Digite um número inteiro '))
fatorial = n
resultado = n
while fatorial != 1:
    print(' {} x'.format(fatorial), end= '')
    fatorial = fatorial - 1
    resultado = resultado * fatorial

print(' 1 = {}'.format(resultado))
print('O valor de {}! é {}'.format(n, resultado))

