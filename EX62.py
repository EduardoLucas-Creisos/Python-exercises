'''Exercício Python 62: Melhore o DESAFIO 61, perguntando
para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''

n = int(input('Digite o primeiro termo '))
r = int(input('Digite a razão '))
s = n
x = int(input('Quantos termos você quer mostrar? '))
y = 0
while x != -1:

    print(' {} -->'.format(s), end='')
    s = s + r
    x = x-1
    if x == 0:
        print(' Pausa')
        print('\nVocê quer ver mais termos? [S/N] ')
        conf = input('Digite S para sim ou N para não ').upper()
        if conf == 'S':
            x = int(input('Quantos termos você quer mostrar? '))
            y = int (input('Você quer continuar de onde parou ou resetar a progressão?'
                           '\n 1-Para continuar \n 2-Para resetar '))
            if y == 1:
                pass
            elif y == 2:
                s = 0
            else:
                print('Opção inválida')
                while y != 1 and y != 2:
                    y = int(input('Você quer continuar de onde parou ou resetar a progressão?'
                                  '\n 1-Para continuar \n 2-Para resetar '))
                    if y == 1:
                        pass
                    elif y == 2:
                        s = 0
                    else:
                        print('Opção inválida')
        elif conf == 'N':
            x = -1
        else:
            print('Opção inválida')
            while conf != 'N' and conf != 'S':
                conf = input('Digite S para sim ou N para não ').upper()
                if conf == 'S':
                    x = int(input('Quantos termos você quer mostrar? '))
                    y = int(input('Você quer continuar de onde parou ou resetar a progressão?'
                                  '\n 1-Para continuar \n 2-Para resetar '))
                    if y == 1:
                        pass
                    elif y == 2:
                        s = 0
                    else:
                        print('Opção inválida')
                        while y != 1 and y != 2:
                            y = int(input('Você quer continuar de onde parou ou resetar a progressão?'
                                          '\n 1-Para continuar \n 2-Para resetar '))
                            if y == 1:
                                pass
                            elif y == 2:
                                s = 0
                            else:
                                print('Opção inválida')
                elif conf == 'N':
                    x = -1
                else:
                    print('Opção inválida')




print('FIM!')
