#leia um número  que vá de 0 a 9999 e mostre na tela cada um de seus digitos separados

num = int(input('Digite um número entre 0 e 9999 '))
m = num // 1000 % 10
c = num // 100 % 10
d = num // 10 % 10
u = num // 1 % 10
print('{} milhar'.format(m))
print('{} centenas'.format(c))
print('{} dezenas'.format(d))
print('{} unidades'.format(u))
