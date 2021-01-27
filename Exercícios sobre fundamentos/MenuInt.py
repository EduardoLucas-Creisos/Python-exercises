x = int(0)
ma = int(0)
me = int(0)
m = int(0)
y = int(0)
s = int(0)
b = int(0)

while x > -1:

    if x == 0 or x == 1:
        n = int(input('Digite um inteiro '))
        ma = n
        me = n

    if x > 0 and x > 1:
        if n > ma:
            ma = n
        if n < me:
            me = n

        y = int(input('Escolha uma opção \n [1] Calcular média \n [2] Mostrar o maior valor \n [3]'
                      ' mostrar o menor valor \n [4] Digitar mais números \n [5] Parar '))
        if y == 1:
            print('A média é {}'.format(m / x))
        elif y == 2:
            print('O maior valor é {}'.format(ma))
        elif y == 3:
            print('O menor valor é {}'.format(me))
        elif y == 4:
            n = int(input('Digite um inteiro '))
        elif y == 5:
            print('Fim!')
            x = -1
        else:
            print('Opção inválida')
            while y != 1 and y != 2 and y != 3 and y != 4 and y != 5:
                b = int(input('Escolha uma opção \n [1] Calcular média \n [2] Mostrar o maior valor \n [3]'
                              ' mostrar o menor valor \n [4] Digitar mais números \n [5] Parar '))
                print('oi')
                if b == 1:
                    print('A média é {}'.format(m / x))
                    y = 1
                elif b == 2:
                    print('O maior valor é {}'.format(ma))
                    y = 2
                elif b == 3:
                    print('O menor valor é {}'.format(me))
                    y = 3
                elif b == 4:
                    n = int(input('Digite um inteiro '))
                    y = 4
                elif b == 5:
                    y = 5
                    print('Fim!')
                    x = -1
                else:
                    print('Opção inválida')

    if x > -1:
        x += 1
    m += n





