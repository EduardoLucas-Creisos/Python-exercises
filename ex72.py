'''Exercício Python 72:
 Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso,
 de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
 mostrá-lo por extenso.'''

numeros = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
           'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte ')
x = 0
while True:
    x = int(input('Escolha um número entre 1 e 20 '))


    if x > 20 :
        break
    print(numeros[x])
    print('Caso queira encerrar o programa digite algum número maior que 20 ')