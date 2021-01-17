#digite o nome de uma cidade e diga se ela começa com o nome Santo
nome = input('Digtie o nome da cidade ')
n = nome.split()
print('A cidade {} começa com Santo? {}'.format(nome, 'Santo' in n))
