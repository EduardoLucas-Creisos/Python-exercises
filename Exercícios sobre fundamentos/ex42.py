#Exercício Python 42: Refaça o DESAFIO 34 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

l1 = int(input('Digite o tamanho de uma reta '))
l2 = int(input('Digite o tamanho de uma reta '))
l3 = int(input('Digite o tamanho de uma reta '))


if l3 < l1+l2 and l2 < l1+l3 and l1 < l3+l2:
    print('O triângulo é possível')
    if (l1 == l2 and l2 == l3 and l1 == l3):
        print('O triângulo é equilátero')
    elif (l1 != l2 and l1 != l3 and l2 != l3):
        print('O triângulo é escaleno')
    else:
        print('O triângulo é isóceles')
else:
    print('O triângulo não é possível')

