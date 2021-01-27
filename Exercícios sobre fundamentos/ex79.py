'''Exercício Python 079:
 Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele
não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''
x = []
n = 0
y = 0
cont = 0
while True:
    n = int(input('Digite um valor inteiro '))
    if n not in x:
        x.append(n)
        print('Valor adicionado')
    else:
        print('Valor não adicionado')
    cont += 1
    y = int(input('Quer continuar colocando valores?\n'
                  '1-para continuar \n'
                  'qualque outro valor para sair '))
    if y != 1:
        break
print(f'A sua lista de forma ordenada{sorted(x)}')