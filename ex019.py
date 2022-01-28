"""Um professor quer sortear um dos quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome
deles a escrevendo o nome do escolhido"""
import random
print('====TESTE 01====')
nome1 = input('Primeiro aluno: ')
nome2 = input('Segundo aluno: ')
nome3 = input('Terceiro aluno: ')
nome4 = input('Quarto aluno: ')
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {} \n'.format(escolhido))

print('====TESTE 02====')
from random import choice
nome1 = str(input('Primeiro aluno: '))
nome2 = str(input('Segundo aluno: '))
nome3 = str(input('Terceiro aluno: '))
nome4 = str(input('Quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = choice(lista)
print('O aluno escolhido foi {} \n'.format(escolhido))



