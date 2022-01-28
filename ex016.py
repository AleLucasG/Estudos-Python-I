"""Crie um programa que leia um número qualquer pelo teclado e mostre na tela a sua porção inteira.
Ex.: Digite um número: 6.127. O número 6.127 tem o parte inteira 6"""

""" DEPENDENDO DE CADA CASO, NÃO É NECESSARIO USAR O MODULO.
num = float(input('Digite um número: ')
print('A porção inteira de {} é de {}'.format(num, int(num)))"""

from math import trunc
num = float(input('Digite um número: '))
print('A porção inteira de {} é {}'.format(num, trunc(num)))


""" DEPENDENDO DE CADA CASO, NÃO É NECESSARIO USAR O MODULO.
num = float(input('Digite um número: ')
print('A porção inteira de {} é de {}'.format(num, int(num)))"""


