'''Exercício Python 089:
 Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
  No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
  de cada aluno individualmente.

'''

camada0 = list()

while True:
    nome = (str(input('Digite seu nome: ')))
    n1 = float(input('Digite a sua primeira nota: '))
    n2 = float(input('Digite a sua segunda nota: '))
    x =(n1+n2)/2
    camada0.append([nome, [n1, n2], x])



    s = str(input('Quer continuar ?[S/N] ')).strip().lower()
    if s == 's':
        pass
    elif s == 'n':
        break
    else:
        pass


print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
for i, a in enumerate(camada0):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-'*35)
    o = int(input('Escolha o numero de um aluno para mostrar as notas dele: (999 interrompe o processo) '))
    if 0 == 999:
        print('Fim')
        break
    if o <= len(camada0)-1:
        print(f'As notas do aluno {camada0[o][0]} são {camada0[o][1]}')
print('fim')
