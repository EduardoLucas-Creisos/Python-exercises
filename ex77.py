'''Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras
 (não usar acentos). Depois disso, você deve mostrar, para cada palavra
 , quais são as suas vogais.'''

n = str('cachorro'), str('gato'), str('macaco'), str('passaro')

for c in n:
    print(f'\nNa palavra {c} temos ')
    for l in c:
      if l.lower() in 'aeiou':
          print(f'{l}', end= ' ')

