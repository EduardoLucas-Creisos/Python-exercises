#digite a largura e a altura de uma parede e depois calcule a área e depois mostre a quantidade de litros
#necessários para pintar uma parede lembrando que cada litro pinta 2 metros quadrados

alt = float(input('Digite a altura da parede '))
lar = float(input('Digite a largura da parede '))
a = alt*lar
ln=a/2
print('A parede tem área de {} e será necessário {} litros de tinta para pintala'.format(a, ln))
