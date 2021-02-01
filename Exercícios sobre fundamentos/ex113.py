#Exercício Python 113: Reescreva a função leiaInt()
# que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo
# inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print('Valor inválido digite novamente')
        except (KeyboardInterrupt):
            print('O usúario preferiu não digitar')
            return 0
        else:
            return n


def LeiaFloat(msg):
    while True:
        try:
            n = float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print('Valor inválido digite novamente')
        except (KeyboardInterrupt):
            print('O usúario preferiu não digitar')
            return 0
        else:
            return n


n1 = leiaInt('Escreva um número inteiro: ')
n2 = LeiaFloat('Digite um número real: ')
print(f'inteiro {n1}\nreal {n2}')



