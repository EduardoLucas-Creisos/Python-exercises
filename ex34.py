#Exercício Python 034: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
l1 = int(input('Digite o tamanho de uma reta '))
l2 = int(input('Digite o tamanho de uma reta '))
l3 = int(input('Digite o tamanho de uma reta '))


if l3 < l1+l2 and l2 < l1+l3 and l1 < l3+l2:
    print('O triângulo é possível')
else:
    print('O triângulo não é possível')