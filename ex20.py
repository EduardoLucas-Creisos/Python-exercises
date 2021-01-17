#Um professor quer sortear a ordem que os alunos devem apresentar o trabalho
import random
a11 = input('Digite o nome de um aluno ')
a12 = input('Digite o nome de um aluno ')
a13 = input('Digite o nome de um aluno ')
a14 = input('Digite o nome de um aluno ')
a1 = 'Carlos'
a2 = 'Flavia'
a3 = 'José'
a4 = 'João'
a5 = 'Maria'
a6 = 'Marcos'
a7 = 'Fernando'
a8 = 'Laura'
a9 = 'Beatriz'
a0 = 'Cristiano'
lista = (a1, a2, a3, a4, a5, a6, a7, a8, a9, a0, a11, a12, a13, a14)
ae = random.choice(lista)
print('A ordem é {}'.format(lista))