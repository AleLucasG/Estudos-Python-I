print()
print('Desafio 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.')
print('')

import math
#from math import trunc
num = float(input('Digite um número: '))
valorInt = math.trunc(num)
#valorInt = trunc(num)
print()

print(f'A porção inteira de {num} é igual a {valorInt}')
print('A porção inteira de {} é igual a {}'.format(num, valorInt))

#sem precisar importar modulo
print('A porção inteira de {} é igual a {}'.format(num, int(num)))