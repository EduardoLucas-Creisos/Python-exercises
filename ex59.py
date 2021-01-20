'''Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.'''



x = 0
n1 = float(input('Digite um número real '))
n2 = float(input('Digite outro número real '))
resultadods = float(0)
while x != 5:
    x = int(input('---------------------------------\nEscolha uma das opões a seguir: \n [1] Somar'
                  ' \n [2] multiplicar \n [3] maior '
                  '\n [4] novos números  \n [5] sair do programa \n---------------------------------'))
    if x == 1:
        resultadods = n1 + n2
        print('O resultado é {} '.format(resultadods))
    elif x == 2:
        resultadods = n1 * n2
        print('O resultado é {} '.format(resultadods))
    elif x == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        else:
            print('{} é maior que {}'.format(n2, n1))
    elif x == 4:
        print('Digite novos números')
        n1 = float(input('Digite um número real '))
        n2 = float(input('Digite outro número real '))
    elif x == 5:
        pass
    else:
        print('Opção inválida tente novamente')





