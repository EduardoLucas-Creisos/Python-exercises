#escreva um programa para aprovação de empréstimo bancário para compra de uma casa.
#o programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
#calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então
# o empréstimo será negado


preço = float(input('Digite o valor da casa '))
sal = float(input('Digite o seu salário '))
anos = int(input('Em quantos anos você quer pagar '))

prest = (preço/12)/anos
sa = sal*0.3
print('Para pagar uma casa de {} com o salário de {} em '.format(preço, sal), end='')
print( '{} anos será necessário pagar {:.2f} por mês'.format(anos, prest))
if(prest > sa):
    print('O valor das prestações excede 30% do seu salário')
    print('Empréstimo negado')
else:
    print('O empréstimo foi aceito')