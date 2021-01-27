#Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida

peso = float(input('Digite seu peso '))
altura = float(input('Digite sua altura '))
imc = peso/altura**2
if(imc < 18.5):
    print('O seu imc é {:.2f} logo você está abaixo do peso'.format(imc))
elif(imc >=18.5 and imc < 25 ):
    print('O seu imc é {:.2f} logo você está no seu peso ideal'.format(imc))
elif(imc >=25 and imc < 30 ):
    print('O seu imc é {:.2f} logo você está com sobrepeso '.format(imc))
elif(imc >=30 and imc < 40 ):
    print('O seu imc é {:.2f} logo você está obeso'.format(imc))
else:
    print('O seu imc é {:.2f} logo você está com obesidade mórbida'.format(imc))