'''Exercício Python 083:
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
 Seu aplicativo deverá
 analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''

ex = str(input('Digite uma expressão '))
l =[]
for x in ex:
    if x == '(':
        l.append('(')
    elif x == ')':
        if len(l) > 0:
            l.pop()
        else:
            l.append(')')
            break
if len(l) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')
