#pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias que ele
#foi alugado. calucole o preço a pagar, sabendo que o carro custa 60 reais por dia e
# 15 centavos de reais por km rodados

dias = int(input('Digite a quantidade de dias que o carro foi alugado '))
km = float(input('Digite a quantidade de Kms rodados '))
preço= dias*60+km*0.15
print('Apó alugar o carro por {} dias e percorrer {}Kms o preço a pagar é {} '.format(dias, km, preço))
