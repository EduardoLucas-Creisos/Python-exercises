#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

idade = int(input('Digite sua idade '))

if(idade > 25):
    print('Você está na categoria Master')
elif(idade <= 25 and idade >19):
    print('Você está na categoria Sênior')
elif(idade <= 19 and idade > 14):
    print('Você está na categoria Júnior')
elif(idade <= 14 and idade > 9):
    print('Você está na categoria Infantil')
else:
    print('Você está na categoria Mirim')