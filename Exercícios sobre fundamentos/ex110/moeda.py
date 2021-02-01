def aumentar(f):
    y = float(input('Digite quanto quer aumentar em %: '))
    f = f * (1+(y/100))
    return (f'O valor aumentado em {y}% é igual a {f}')


def diminiuir(f):
    y = float(input('Digite quanto quer diminuir em %: '))
    f = f * (y/100)
    return (f'O valor diminuído em {y}% é igual a {f}')


def dobrar (f):
    f = f*2
    return (f'O valor de {f} dobreado ')


def metade (f):
    f = f/2
    return (f'O valor de {f} pela metade é: ')


