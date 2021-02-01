#Exercício Python 108: Adapte o código do desafio #107,
# criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.


import moeda

f = int(input('Digite o valor em R$ '))
print(f'O valor aumentado de R${f} em 30% é R${moeda.aumentar(f):<.2f} ')
print(f'O valor diminuido em R${f} 20% é R${moeda.diminiuir(f):<.2f}')
print(f'O valor dobrado de R${f} é R${moeda.dobrar(f):<.2f}')
print(f'O valor pela metade de R${f} é R${moeda.metade(f):<.2f}')