print()
print('Desafio 11: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área \n'
      'e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.')
print()

largura = float(input('Qual a largura da parede: '))
altura = float(input('Qual a altura da parede: '))
area = largura * altura
litros = area / 2
print()
print('Sua parede tem a dimensão de {}x{} e sua área é {}m²'.format(largura,altura, area))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta'.format(litros))
