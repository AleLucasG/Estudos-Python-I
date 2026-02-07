print()
print('Desafio 005: Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.')
print()
valor = int(input('Digite um valor: '))
sucessor = valor + 1
antecessor = valor - 1
print('O sucessor de {} é {}, e o antecessor é {}'.format(valor, sucessor, antecessor))