#Exercício Python 49: Refaça o DESAFIO 9,
# mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n = int(input('Digite um inteiro qualquer '))

for c in range(0, 11):
    print('{} x {} é igual á {}'.format(n, c, n*c))

