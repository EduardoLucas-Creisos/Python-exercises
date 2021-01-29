'''Exercício Python 106:
 Faça um mini-sistema que utilize o Interactive Help do Python.
  O usuário vai digitar o comando e o manual vai aparecer.
 Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.'''
c = ('\033[0;30;41m', #vermelho
     '\033[0;30;42m', #verde
     '\033[0;30;43m', #amarelo
     '\033[0;30;44m', #azul
     '\033[0;30;45m', #roxo
     '\033[7;30m'
);
import time
def ajuda(comando):
    tit(f'Checando \'{comando}\'',4)
    time.sleep(1)
    print(help(comando))
    print(c[5],end='')
def tit(msg, cor = 3):
    tam = len(msg)+4
    print(c[cor], end='')
    print('=-='*tam)
    print('{:^28}'.format(msg))
    print('=-=' *tam)
    print(c[cor],end='')
    time.sleep(1)


while True:
    tit('Manual')
    v = str(input('Digite o nome da função desejada: (DIGITE FIM PARA FINALIZAR) ')).lower()

    time.sleep(0.5)
    if v in 'fim':
        print(c[3],end='')
        print('Finalizando')
        break
    ajuda(v)







