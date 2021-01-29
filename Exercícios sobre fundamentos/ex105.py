'''Exercício Python 105:
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:

– Quantidade de notas
– A maior nota
– A menor nota
 – A média da turma
  – A situação (opcional)

'''

def notas(*num, sit = False):
    """

    :param num: Uma ou mais notas dos alunos
    :param sit: Escplha se quer ou não checar a situação dos alunos
    :return: Um dicionário com várias informações sobre a turma
    """
    r = dict()
    r['total'] = len(num)
    r['maior'] = max(num)
    r['menor'] = min(num)
    r['média'] = sum(num)/len(num)
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'ACEITÁVEL'
        else:
            r['situação'] = 'RUIM'
    return r




#main
resp = notas(9, 3, 4, 5, 6, sit=True)
print(resp)
#help(notas)
