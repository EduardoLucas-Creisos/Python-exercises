#Exercício Python 033: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Digite o Salário para calculo do aumento '))
if sal > 1250:
    sal = sal * 1.1
else:
    sal = sal * 1.15

print('O novo salário é {:.2f}R$'.format(sal))