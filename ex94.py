'''Exercício Python 094:
Crie um programa que leia nome,
sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
 No final, mostre: A) Quantas pessoas foram cadastradas
  B) A média de idade
  C) Uma lista com as mulheres
  D) Uma lista de pessoas com idade acima da média'''

lista = list()
dados = dict()
s = ''
media = 0
cont = 0

while True:
    dados['nome'] = str(input('Digite seu nome: '))
    dados['sexo'] =  str(input(('Digite seu sexo: [M/F] '))).lower()[0]
    dados['idade'] = int(input('Digite sua idade: '))
    media += dados['idade']

    lista.append(dados.copy())
    s = str(input('Quer continuar? [S/N] ')).strip().lower()
    cont += 1
    if s[0] == 'n':
        break
    else:
        pass

media = media/cont


print(f'A) Temos {cont} pessoas cadastradas')
print(f'B) A média de idade é {media:5.2f}')
print(f'C) as mulheres cadastradas são: ',end='')
for dados in lista:
    if dados['sexo'] in 'f':
        print(f' {dados["nome"]},',end='')
print()
print('D) A lista de pessoas com idade acima da média é: ')
for dados in lista:
    if dados['idade'] > media:
        for k, v in dados.items():
            print(f' {k} = {v}', end='')


