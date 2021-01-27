#Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros

preço = float(input('Digite o preço do produto em R$ '))

print('Ecolha o método de pagamento')
print('1-À vista dinheiro/cheque: 10% de desconto')
print('2-À vista no cartão: 5% de desconto')
print('3-Em até 2x no cartão: preço formal ')
print('4-3x ou mais no cartão: 20% de juros')
x = int(input('Escolha a opção desejada '))
if (x == 1):
     print('O valor do produto fica por {}R$'.format(preço*0.9))
elif(x == 2):
      print('O valor do produto fica por {}R$'.format(preço*0.95))
elif(x == 3):
      print('O produto de valor {}R$ fica por 2 parcelas de {}R$'.format(preço, preço/2))
elif(x == 4):
    parcelas = int(input('Escolha o número de parcelas que você quer dividir '))
    if(parcelas == 2):
        print('O produto de valor {}R$ fica por 2 parcelas de {}R$ sem juros'.format(preço, preço / 2))
    elif(parcelas > 2):
        preçototal = preço*1.2
        valorparcela = preçototal/parcelas
        print('O novo valor é {}R$ dividido em {} parcelas no valor de {}R$ '.format(preçototal, parcelas, valorparcela))
    else:
        print('O valor do produto fica por {}R$'.format(preço * 0.95))
else:
    print('Opção inválida')