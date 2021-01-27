#027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente
nome = input('Digite o nome completo ')
nome = nome.split()
print('O primeiro nome é {}'.format(nome[0]))
print('O último nome é {}'.format(nome[(len(nome)-1)]))
