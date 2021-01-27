#calcule a hipotenusa
import math
cato = float(input('Digite o comprimento do cateto oposto '))
cata = float(input('Digite o comprimmento do cateto adjacente '))
hip = math.hypot(cato, cata)
hipo = math.sqrt(pow(cata, 2) + pow(cato, 2))
print('A hipotenusa do triângulo é {:.2f}'.format(math.hypot(cato, cata)))
print('A hipotenusa do triângulo é {:.2f}'.format(hip))
print('A hipotenusa do triângulo é {:.2f}'.format(hipo))