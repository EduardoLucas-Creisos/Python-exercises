def nome(msg):
    s = str(input(msg))
    return s


def idade(msg):
    x = str(input(msg))
    if x.isnumeric() == True:
        pass
    else:
        x = str(input('Idade inválida digite novamente: '))
        while x.isnumeric() == False:
            x = str(input('Idade inválida digite novamente: '))
    return x
