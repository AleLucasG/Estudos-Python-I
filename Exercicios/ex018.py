import math
#from math import sin, cos, tan

print()
print('Desafio 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.')
print('Seno do ângulo = sen(ângulo)\n'
      'Cosseno do ângulo = cos(ângulo)\n'
      'Tangente do ângulo = tg(ângulo)\n'
      'Se o ângulo estiver em graus: Radianos = graus × π / 180')
print()

angulo = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O angulo de {}, tem o SENO de {:.2f}'.format(angulo, seno))
print('O angulo de {}, tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print('O angulo de {}, tem o TANGENTE de {:.2f}'.format(angulo, tangente))