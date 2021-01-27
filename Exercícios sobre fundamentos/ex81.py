'''Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
   Depois disso, mostre:
  A) Quantos números foram digitados.
  B) A lista de valores, ordenada de forma decrescente.
  C) Se o valor 5 foi digitado e está ou não na lista'''

x = []
y = 0
cont = 0
while True:
    x.append(int(input('Digite um valor inteiro ')))
    cont += 1
    y = int(input('Quer continuar colocando valores?\n'
                  '1-para continuar \n'
                  'qualque outro valor para sair '))
    if y != 1:
        break

print(f'O total de números digitados foi {cont}')
print(f'A lista de forma ordenada fica da seguinte forma {sorted(x)}')
if 5 in x:
    print('O valor 5 está na lista ')



