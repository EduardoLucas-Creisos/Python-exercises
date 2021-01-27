'''Exercício Python 093:
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai
ler o nome do jogador e quantas partidas ele jogou.
 Depois vai ler a quantidade de gols feitos em cada partida. No final,
tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.'''


jogador = dict()
soma = 0
jogador['nome'] = str(input('Digite o nome do jogador: '))
jogador['npartidas'] = int(input('Quantas partidas ele jogou? '))
partidas = list()
for c in range (0 , jogador['npartidas']):
    jogador['gols'] = int(input(f'Quantos gols ele marcou na {c+1}° partida ? '))
    soma += jogador['gols']
    partidas.append(jogador['gols'])

print(f'O jogador {jogador["nome"]}')
print(f'Jogou {jogador["npartidas"]} partidas')
print('-='*30)
for g in enumerate(partidas):
    print(f'Jogo {g[0]+1} ----- {partidas[g[0]]} gols marcados')
    print('-'*20)
print('-='*30)
print('No total foram {} gols em um total de  {} jogos'.format(soma, jogador['npartidas']))
print('-='*30)