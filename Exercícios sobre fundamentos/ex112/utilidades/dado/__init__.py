def leiaDinheiro(x):
    y = str(input(f'{x}'))

    try:
        return int(y)
    except ValueError:
        try:
            if ',' in y:
                y = y.replace(',', '.')
            return float(y)
        except ValueError:
            pass

    if y.isnumeric() == False:
        print('Opção inválida: ')
        y = str(input(f'{x}'))
        while y.isnumeric() == False:
            print('Opção inválida: ')
            y = str(input(f'{x}'))


    if ',' in y:
        y = y.replace(',', '.')


    try:
        return int(y)
    except ValueError:
        return float(y)


