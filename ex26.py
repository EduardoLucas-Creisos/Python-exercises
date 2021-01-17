#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Digite Qualquer frase: ')
print('A letra "a" aparece {} vezes na frase   '.format(frase.count('a') ))
print('A primeira vez que ela aparece é na {}° posição a última posição que ela aparece é {}° '.format(frase.find('a'), frase.rfind('a')))