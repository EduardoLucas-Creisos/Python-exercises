#digite uma temperatura em celsius e mostre ela em farenheit
c = float(input("Digite a temperatura em C° "))
f = (c*1.8)+32
k= c+273.15
print('A temperatura {:.2f} em C° é equivalente a {:.2f} F° e equivalente a {:.2f} K° '.format(c, f, k))