print()
print('Desafio 30: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.')
print()

import time
print('====== O NÚMERO É PAR OU IMPAR? =====')
print()

num = int(input('Digite um número e lhe direi se ele é par ou impar: '))
print('Processando...')
time.sleep(2)

resultado = num % 2

if resultado == 0:
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é impar.')