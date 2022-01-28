"""Crie um algoritmo que leia um número e mostra o seu dobro, triplo e raiz quadrada"""

n1 = int(input("Digite um número: "))
print('O dobro de {} é {}.'.format(n1, n1*2))
print('O triplo de {} é {}.' .format(n1, n1*3))
print('A raiz quadrada de {} é {:.2f}. \n' .format(n1, n1**(1/2)))

"""Como Guanabara fez"""

n = int(input("Digite um número: "))
print('O dobro de {} é {}.'.format(n, n*2))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.' .format(n, (n*3), n, pow(n,(1/2))))






