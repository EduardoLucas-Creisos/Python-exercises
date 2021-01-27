#leia um ângulo qualquer e mostre seu seno, cosseno e tangente na tela
import math
ang = float(input('Digtie um ângulo qualquer '))
sin = math.sin(ang)
cos = math.cos(ang)
tan = math.tan(ang)
print('O ângulo {:.5f} tem seno igual a {:.5f} e cosseno igual a {:.5f} e tangente igual a {:.5f} '.format(ang, sin, cos, tan))