print('Desafio 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.\n'
      ' Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.')
print()

print('============ SORTEIO DA TURMA ============')
print('===== ORDEM DE APRESENTAÇÃO DOS TRABALHOS =====')
print()

import random
aluno1 = str(input('Nome do aluno1: '))
aluno2 = str(input('Nome do aluno2: '))
aluno3 = str(input('Nome do aluno3: '))
aluno4 = str(input('Nome do aluno4: '))

lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)

print('A ordem de apresentação é: {}.'.format(lista))