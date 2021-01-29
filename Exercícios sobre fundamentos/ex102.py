'''Exercício Python 102:
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
 o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico
(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.'''
from typing import Any, Tuple


def fatorial(num=0, op=False):
    """
    :param num: Digite sempre este parâmetro para calcular o fatorial de um número inteiro
    :param op(opcional): Digite este valor para ver o processo de calculo
    :return: O valor do fatorial e caso queira o processo de calculo
    """
    y = int(1)
    x = list()
    max = 0
    for c in range(0, num, 1):
        y *= num-c
        x.append(y)
    x.pop()
    max = len(x)-1
    if op == True:
        def true():
            print(f'O calculo funcionou do seguinte modo ',end=' ')
            for c in range(0,len(x)):
                print(f'{x[c]} ',end='')
                if c != max:
                    print(' X ',end='')
            print(f'Igual a {y}')
        return true()
    else:
        return print(f'O resultado foi {y}')


#main


xe=fatorial(4,True)

'''Resolução simples 
def fatorial (num,show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end = '')
        else
            print(' = ', end = '')
        f*=c
    return f

'''