"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, calcule e mostre o
comprimento da hipotenusa a² = b² + c².
- a: Hipotenusa
- b: Cateto Oposto
- c: Cateto Adjacente"""

print('=====TESTE 01 - SEM METODO=====')
co = float(input('Qual o comprimento dp Cateto Oposto: '))
ca = float(input('Qual o comprimento do Cateto Adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f} \n'.format(hi))

print('=====TESTE 02 - COM METODO=====')
import math
co = float(input('Qual o comprimento dp Cateto Oposto: '))
ca = float(input('Qual o comprimento do Cateto Adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f} \n'.format(hi))

print('=====TESTE 03 - COM METODO=====')
from math import hypot
co = float(input('Qual o comprimento dp Cateto Oposto: '))
ca = float(input('Qual o comprimento do Cateto Adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f} \n'.format(hi))









