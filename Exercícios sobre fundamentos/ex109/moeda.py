def aumentar(f):
    f = f * 1.3
    return f


def diminiuir(f):
    f = f * 0.8
    return f


def dobrar (f):
    f = f*2
    return f


def metade (f):
    f = f/2
    return f


def resumo(f):
    l = list()
    l.append(f'R${f}   com aumento de 30%:       R${aumentar(f):<.2f}')
    l.append(f'R${f}   diminuido em 20%:         R${diminiuir(f):<.2f}')
    l.append(f'R${f}   dobrado:                  R${dobrar(f):<.2f}')
    l.append(f'R${f}   pela metade:              R${metade(f):<.2f}')
    t = (len(l[2])+6)
    tam = ('-'*t)
    return       (f'{tam}\n'
                 'VALOR:  OPERAÇÃO                  RESULTADO:\n'
                 f'{l[0]}\n'
                 f'{l[1]}\n'
                 f'{l[2]}\n'
                 f'{l[3]}\n'
                 f'{tam}\n')