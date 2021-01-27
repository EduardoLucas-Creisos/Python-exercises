'''Exercício Python 080:
 Crie um programa onde o usuário possa digitar cinco
  valores numéricos e cadastre-os em uma lista,
 já na posição correta de inserção (sem usar o sort()). No final,
  mostre a lista ordenada na tela.'''

x = 0
l = []

for c in range(0, 5):
    x = (int(input('Digite um valor inteiro ')))
    if c == 0 or x > l[-1]:
        l.append(x)
    else:
        p = 0
        while p < len(l):
            if x <= l[p]:
                l.insert(p , x)
                break
            p += 1

print(l)



