print()
print('Desafio 17: Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. \n'
      'Calcule e mostre o comprimento da hipotenusa.')
print('Formula: hipotenusa = (co**2 + ca**2) ** 0.5')
print()

import math
#from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hipotenusa = math.hypot(co, ca)
#hipotenusa = hypot(co, ca)
print()

print('A medida da hipotenusa é {}'.format(hipotenusa))
print('A medida da hipotenusa é {:.2f}'.format(hipotenusa))
print('A medida da hipotenusa é {:.3f}'.format((co**2 + ca**2)**0.5))

