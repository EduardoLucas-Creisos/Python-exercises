'''Exercício Python 090:
 Faça um programa que leia nome e média de um aluno, guardando também
 a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

'''

aluno = dict()

aluno ['nome'] = str(input('Digite o nome do aluno: '))
aluno ['media'] = float(input('Digite  a média do aluno: '))
print()
print(f'O nome do aluno é {aluno["nome"]}')
print(f'A média do aluno é {aluno["media"]}')
if aluno['media'] >= 7:
    print('O aluno está aprovado ')
elif aluno['media'] > 5 and aluno['media'] < 7:
    print('O aluno está de recuperação')
else:
    print('O aluno está reprovado')