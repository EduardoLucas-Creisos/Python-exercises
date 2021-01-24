'''Exercício Python 076:
 Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
 na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''


t = ('lápis', 1.70, 'borracha', 2, 'caderno', 10, 'lanche', 15, 'caneta', 2.50)

for x in range(0, len(t)):
    if x % 2 == 0:
        print(f'{t[x]:.<20}', end= '')
    if x % 2 != 0:
        print('R${}'.format(t[x]))

