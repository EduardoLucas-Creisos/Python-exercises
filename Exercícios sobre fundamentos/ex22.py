#leia um nome completo e imprima ele com letras maisculas, minusculas quantos caracteres ele tem sem considerar espaços
#e quantas letras tem o primeiro nome

nome = input('Digite seu nome completo ')
name = nome.split()

print('Seu nome em caixa maior é {}'.format(nome.upper()))
print('Seu nome em caixa menor é {} '.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(len(name[0])))