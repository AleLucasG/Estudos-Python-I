print()
print('Desafio 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.')
print()
valor = int(input('Digite um valor: '))
dobro = valor * 2
triplo = valor * 3
raiz = valor ** (1/2)
print('O dobro de {0} é {1}. O triplo de {0} é {2} e a raiz quadrada de {0} é {3}'.format(valor, dobro, triplo, raiz))
print('O dobro de {0} é {1}. O triplo de {0} é {2} e a raiz quadrada de {0} é {3:.2f}'
      .format(valor, dobro, triplo, raiz))