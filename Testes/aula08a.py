import math
#from math import sqrt
print()

num = int(input('Digite um valor: '))
raiz = math.sqrt(num)
#raiz = sqrt(num)
print()

print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
print(f'A raiz de {num} é igual a {math.ceil(raiz)}')
print(f'A raiz de {num} é igual a {math.floor(raiz)}')