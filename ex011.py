"""Faça um programa que leia a largura e a altura de uma parede em metros.
Calcule a sua área e a quantidade de tinta necessaria p/ pintá-la.
Sabendo que cada litro de tinta pinta uma área de 2m²"""

largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = largura * altura
litros = area / 2
print('A àrea da parede é de {:.3f} m². \nPara pintar essa parede, você precisará de {} litros de tinta.' .format(area, litros))






