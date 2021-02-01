#Exercício Python 107:
#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(),
#dobro() e metade(). Faça também um programa que importe esse módulo e use algumas dessas funções.

import moeda

f = int(input('Digite o valor em R$ '))
print(f'O valor aumentado de R${f} em 30% é R${moeda.aumentar(f)} ')
print(f'O valor diminuido em R${f} 20% é R${moeda.diminiuir(f)}')
print(f'O valor dobrado de R${f} é R${moeda.dobrar(f)}')
print(f'O valor pela metade de R${f} é R${moeda.metade(f)}')