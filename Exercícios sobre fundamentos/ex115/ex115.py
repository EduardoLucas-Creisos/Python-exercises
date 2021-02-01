#faça um menu que armazene pessoas e suas idades em um arquivo txt

import cadastro
import time
s = '          '
v = '\n'
lista = list()
x = 0
l = list()
arquivo = open('lista.txt', 'a')
while True:
    x = int(input('1-Para cadastrar um usuário\n2-Para ler a lista de usuários cadastrados\n3-Para sair\n'))
    if x == 1:
        lista.append(cadastro.nome('Digite seu nome: ').ljust(15))
        lista.append(cadastro.idade('Digite sua idade: ').center(5)+v)
        arquivo.writelines(lista)
        l.append(lista[:])
        lista.clear()
    elif x == 2:
        print('-'*30)
        arquivo = open('lista.txt','r')
        for v in arquivo:
            print(v)
        print('-'*30)
    elif x == 3:
        print('Finalizando')
        for c in range(1,5):
            time.sleep(0.9)
            print('.')
        break

    else:
        while x != 1 and x != 2 and x != 3:
            print('Opção inválida tente novamente')
            x = int(input('1-Para cadastrar um usuário\n2-Para ler a lista de usuários cadastrados\n3-Para sair'))

