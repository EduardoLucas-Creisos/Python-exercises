'''Exercício Python 73:
 Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
  na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.'''

times = ('PALMEIRAS', 'FLAMENGO', 'INTERNACIONAL', 'GRÊMIO', 'SÃO PAULO', 'ATLÉTICO-MG', 'ATLÉTICO-PR',
         'CRUZEIRO', 'BOTAFOGO', 'SANTOS', 'BAHIA', 'FLUMINENSE', 'CORINTHIANS', 'CHAPECOENSE', 'CEARÁ SC',
         'VASCO DA GAMA', 'SPORT RECIFE', 'AMÉRIICA-MG', 'EC VITÓRIA', 'PARANÁ')

print('Os primeiros colocados foram:')
for c in range(0, 5):
    print(times[c])
print('Os últimos colocados foram: ')
for x in range(16, 20):
    print(times[x])

print('Os times em ordem alfabética')
print(sorted(times))

print('A chapecoense ficou em {}º lugar'.format(times.index('CHAPECOENSE')+1))

