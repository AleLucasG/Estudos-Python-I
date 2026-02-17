import random
#from randon import choice

print('Desafio 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.\n'
      'Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.')
print()

print('============ SORTEIO DA TURMA ============')
print('===== QUEM VAI APAGAR O QUADRO NEGRO =====')
print()
aluno1 = str(input('Nome do aluno1: '))
aluno2 = str(input('Nome do aluno2: '))
aluno3 = str(input('Nome do aluno3: '))
aluno4 = str(input('Nome do aluno4: '))

opcoes = [aluno1, aluno2, aluno3, aluno4]
sorteado = random.choice(opcoes)

print()
print('O aluno(a) escolhi(a) foi: {}'.format(sorteado))