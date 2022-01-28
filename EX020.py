"""O mesmo professor do desafio 19 quer sortear a ordem de apresentação de um trabalho dos alunos.
Faça um programa que leia o nome de quatro alunos e mostre a ordem sorteada"""

import random
print('=====TESTE 01=====')
n1 = str(input('1° nome: '))
n2 = str(input('2° nome: '))
n3 = str(input('3° nome: '))
n4 = str(input('4° nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de nomes é {} \n'.format(lista))

from random import shuffle
print('=====TESTE 02=====')
n1 = str(input('1° nome: '))
n2 = str(input('2° nome: '))
n3 = str(input('3° nome: '))
n4 = str(input('4° nome: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de nomes é {} \n'.format(lista))




