'''Exercício Python 097:
Faça um programa que tenha uma função chamada escreva(),
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:
escreva(‘Olá, Mundo!’) Saída:

                    ~~~~~~~~~
                    Olá, Mundo!
                    ~~~~~~~~~
 '''

def escreva(b):
    t = len(b)
    print('-'*t)
    print(b)
    print('-'*t)


texto = str(input('Digite algo: '))
escreva(texto)