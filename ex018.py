"""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
sen = co/hi
cos = ca / hi
tan = co / ca"""

print('=====TESTE 01=====')
co = float(input('Digite o valor de cateto oposto: '))
ca = float(input('Digite o valor de cateto adjacente: '))
hi = float(input('Digite o valor da hipotenusa: '))
sen = co / hi
cos = ca / hi
tan = co / ca
print('O Valor de seno:{:.3}, cosseno:{:.3} e tangente é de {:.3} \n'.format(sen, cos, tan))

print('=====TESTE 02=====')
import math
angulo = float(input('Digite o valor do angulo: '))
seno = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2}'.format(angulo, seno))
cos = math.cos(math.radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2}'.format(angulo, cos))
tan = math.tan(math.radians(angulo))
print('O angulo de {} tem o TANGENTE de {:.2} \n'.format(angulo, tan))

print('=====TESTE 03=====')
from math import sin, cos, tan, radians
angulo = float(input('Digite o valor do angulo: '))
seno = sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2}'.format(angulo, seno))
cos = cos(math.radians(angulo))
print('O angulo de {} tem o COSSENO de {:.2}'.format(angulo, cos))
tan = tan(math.radians(angulo))
print('O angulo de {} tem o TANGENTE de {:.2} \n'.format(angulo, tan))













