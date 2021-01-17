#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('Digite o nome completo ')
print('O nome tem {} Silva? {}'.format(nome, 'Silva' in nome))